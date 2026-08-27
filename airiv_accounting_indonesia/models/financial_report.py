# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AirivFinancialReport(models.Model):
    _name = 'airiv.financial.report'
    _description = 'Laporan Keuangan SAK EMKM Indonesia'
    _order = 'date_to desc, id desc'

    name = fields.Char(string="Judul Laporan", required=True)
    report_type = fields.Selection([
        ('laba_rugi', 'Laporan Laba Rugi (Income Statement)'),
        ('neraca', 'Laporan Posisi Keuangan (Neraca / Balance Sheet)'),
        ('arus_kas', 'Laporan Arus Kas (Cash Flow - Direct)'),
    ], string="Jenis Laporan", required=True, default='laba_rugi')

    date_from = fields.Date(string="Dari Tanggal", required=True, default=lambda self: fields.Date.today().replace(month=1, day=1))
    date_to = fields.Date(string="Sampai Tanggal", required=True, default=fields.Date.today)
    company_id = fields.Many2one('res.company', string="Perusahaan", default=lambda self: self.env.company, required=True)

    line_ids = fields.One2many('airiv.financial.report.line', 'report_id', string="Rincian Pos Laporan")

    # Calculated Financial Summary Totals
    total_pendapatan = fields.Monetary(string="Total Pendapatan Usaha", compute="_compute_report_totals", currency_field='currency_id')
    total_hpp = fields.Monetary(string="Total Beban Pokok Penjualan", compute="_compute_report_totals", currency_field='currency_id')
    laba_kotor = fields.Monetary(string="Laba Kotor (Gross Profit)", compute="_compute_report_totals", currency_field='currency_id')
    total_beban_ops = fields.Monetary(string="Total Beban Operasional", compute="_compute_report_totals", currency_field='currency_id')
    laba_bersih = fields.Monetary(string="Laba / (Rugi) Bersih Periode Berjalan", compute="_compute_report_totals", currency_field='currency_id')

    total_aset = fields.Monetary(string="Total Aset", compute="_compute_report_totals", currency_field='currency_id')
    total_liabilitas = fields.Monetary(string="Total Liabilitas", compute="_compute_report_totals", currency_field='currency_id')
    total_ekuitas = fields.Monetary(string="Total Ekuitas", compute="_compute_report_totals", currency_field='currency_id')
    balance_check = fields.Monetary(string="Selisih Neraca (Aset - Liabilitas - Ekuitas)", compute="_compute_report_totals", currency_field='currency_id')

    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string="Mata Uang")
    state = fields.Selection([('draft', 'Draft'), ('calculated', 'Dihitung')], default='draft')

    def action_calculate_report(self):
        self.ensure_one()
        self.line_ids.unlink()

        MoveLine = self.env['account.move.line'].sudo()
        lines_to_create = []

        if self.report_type == 'laba_rugi':
            # 1. Pendapatan (Credit - Debit)
            p_lines = MoveLine.search([
                ('move_id.state', '=', 'posted'),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
                ('company_id', '=', self.company_id.id),
                ('account_id.account_type', 'in', ('income', 'income_other'))
            ])
            acc_p = {}
            for l in p_lines:
                acc_p[l.account_id] = acc_p.get(l.account_id, 0.0) + (l.credit - l.debit)
            for acc, amt in acc_p.items():
                lines_to_create.append({
                    'report_id': self.id,
                    'section': 'pendapatan',
                    'account_id': acc.id,
                    'name': f"[{acc.code}] {acc.name}",
                    'amount': amt
                })

            # 2. HPP (Debit - Credit)
            hpp_lines = MoveLine.search([
                ('move_id.state', '=', 'posted'),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
                ('company_id', '=', self.company_id.id),
                ('account_id.account_type', '=', 'expense_direct_cost')
            ])
            acc_hpp = {}
            for l in hpp_lines:
                acc_hpp[l.account_id] = acc_hpp.get(l.account_id, 0.0) + (l.debit - l.credit)
            for acc, amt in acc_hpp.items():
                lines_to_create.append({
                    'report_id': self.id,
                    'section': 'hpp',
                    'account_id': acc.id,
                    'name': f"[{acc.code}] {acc.name}",
                    'amount': amt
                })

            # 3. Beban Operasional & Lain-lain (Debit - Credit)
            exp_lines = MoveLine.search([
                ('move_id.state', '=', 'posted'),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
                ('company_id', '=', self.company_id.id),
                ('account_id.account_type', 'in', ('expense', 'expense_depreciation'))
            ])
            acc_exp = {}
            for l in exp_lines:
                acc_exp[l.account_id] = acc_exp.get(l.account_id, 0.0) + (l.debit - l.credit)
            for acc, amt in acc_exp.items():
                lines_to_create.append({
                    'report_id': self.id,
                    'section': 'beban_ops',
                    'account_id': acc.id,
                    'name': f"[{acc.code}] {acc.name}",
                    'amount': amt
                })

        elif self.report_type == 'neraca':
            # Aset (Debit - Credit up to date_to)
            aset_lines = MoveLine.search([
                ('move_id.state', '=', 'posted'),
                ('date', '<=', self.date_to),
                ('company_id', '=', self.company_id.id),
                ('account_id.account_type', 'in', ('asset_receivable', 'asset_cash', 'asset_current', 'asset_non_current', 'asset_prepayments', 'asset_fixed'))
            ])
            acc_aset = {}
            for l in aset_lines:
                acc_aset[l.account_id] = acc_aset.get(l.account_id, 0.0) + (l.debit - l.credit)
            for acc, amt in acc_aset.items():
                lines_to_create.append({
                    'report_id': self.id,
                    'section': 'aset',
                    'account_id': acc.id,
                    'name': f"[{acc.code}] {acc.name}",
                    'amount': amt
                })

            # Liabilitas (Credit - Debit up to date_to)
            liab_lines = MoveLine.search([
                ('move_id.state', '=', 'posted'),
                ('date', '<=', self.date_to),
                ('company_id', '=', self.company_id.id),
                ('account_id.account_type', 'in', ('liability_payable', 'liability_credit_card', 'liability_current', 'liability_non_current'))
            ])
            acc_liab = {}
            for l in liab_lines:
                acc_liab[l.account_id] = acc_liab.get(l.account_id, 0.0) + (l.credit - l.debit)
            for acc, amt in acc_liab.items():
                lines_to_create.append({
                    'report_id': self.id,
                    'section': 'liabilitas',
                    'account_id': acc.id,
                    'name': f"[{acc.code}] {acc.name}",
                    'amount': amt
                })

            # Ekuitas (Credit - Debit up to date_to)
            eq_lines = MoveLine.search([
                ('move_id.state', '=', 'posted'),
                ('date', '<=', self.date_to),
                ('company_id', '=', self.company_id.id),
                ('account_id.account_type', 'in', ('equity', 'equity_unaffected'))
            ])
            acc_eq = {}
            for l in eq_lines:
                acc_eq[l.account_id] = acc_eq.get(l.account_id, 0.0) + (l.credit - l.debit)
            for acc, amt in acc_eq.items():
                lines_to_create.append({
                    'report_id': self.id,
                    'section': 'ekuitas',
                    'account_id': acc.id,
                    'name': f"[{acc.code}] {acc.name}",
                    'amount': amt
                })

        if lines_to_create:
            self.env['airiv.financial.report.line'].create(lines_to_create)
        self.state = 'calculated'

    @api.depends('line_ids.amount', 'report_type')
    def _compute_report_totals(self):
        for rec in self:
            p = sum(rec.line_ids.filtered(lambda l: l.section == 'pendapatan').mapped('amount'))
            hpp = sum(rec.line_ids.filtered(lambda l: l.section == 'hpp').mapped('amount'))
            b = sum(rec.line_ids.filtered(lambda l: l.section == 'beban_ops').mapped('amount'))
            
            rec.total_pendapatan = p
            rec.total_hpp = hpp
            rec.laba_kotor = p - hpp
            rec.total_beban_ops = b
            rec.laba_bersih = (p - hpp) - b

            aset = sum(rec.line_ids.filtered(lambda l: l.section == 'aset').mapped('amount'))
            liab = sum(rec.line_ids.filtered(lambda l: l.section == 'liabilitas').mapped('amount'))
            eq = sum(rec.line_ids.filtered(lambda l: l.section == 'ekuitas').mapped('amount'))

            rec.total_aset = aset
            rec.total_liabilitas = liab
            rec.total_ekuitas = eq
            rec.balance_check = aset - (liab + eq)


class AirivFinancialReportLine(models.Model):
    _name = 'airiv.financial.report.line'
    _description = 'Rincian Pos Akun Laporan Keuangan SAK EMKM'
    _order = 'section, id'

    report_id = fields.Many2one('airiv.financial.report', string="Laporan Induk", ondelete='cascade', required=True)
    section = fields.Selection([
        ('pendapatan', 'Pendapatan Usaha'),
        ('hpp', 'Beban Pokok Penjualan'),
        ('beban_ops', 'Beban Operasional & Lain-lain'),
        ('aset', 'Aset'),
        ('liabilitas', 'Liabilitas'),
        ('ekuitas', 'Ekuitas'),
    ], string="Kelompok Akun", required=True)

    account_id = fields.Many2one('account.account', string="Akun Akuntansi")
    name = fields.Char(string="Nama Akun / Deskripsi", required=True)
    amount = fields.Monetary(string="Saldo (Rp)", required=True, default=0.0, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', related='report_id.currency_id')

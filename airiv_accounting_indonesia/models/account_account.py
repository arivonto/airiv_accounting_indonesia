# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountAccount(models.Model):
    _inherit = 'account.account'

    l10n_id_emkm_category = fields.Selection([
        ('aset_lancar', '1.1 Aset Lancar (Kas, Bank, Piutang, Persediaan)'),
        ('aset_tetap', '1.2 Aset Tetap & Akumulasi Penyusutan'),
        ('liabilitas_pendek', '2.1 Liabilitas Jangka Pendek (Utang Usaha, Utang Pajak)'),
        ('liabilitas_panjang', '2.2 Liabilitas Jangka Panjang (Utang Bank/Investasi)'),
        ('ekuitas', '3.1 Ekuitas (Modal Saham, Saldo Laba/Rugi)'),
        ('pendapatan_utama', '4.1 Pendapatan Usaha / Penjualan'),
        ('hpp', '5.1 Beban Pokok Penjualan (HPP)'),
        ('beban_operasional', '6.1 Beban Operasional / Umum & Administrasi'),
        ('pendapatan_lain', '7.1 Pendapatan Lain-lain (Non-Operasional)'),
        ('beban_lain', '7.2 Beban Lain-lain & Pajak Penghasilan'),
    ], string="Kategori SAK EMKM", help="Klasifikasi pelaporan keuangan baku SAK EMKM Indonesia")

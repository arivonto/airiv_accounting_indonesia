# -*- coding: utf-8 -*-
{
    'name': 'Indonesia SAK EMKM Accounting & Financial Reports (Neraca & Laba Rugi)',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Localizations/Account Charts',
    'summary': 'SAK EMKM Chart of Accounts, Indonesian Financial Statements (Laba Rugi, Neraca, Arus Kas), and Tax Mapping for Community',
    'description': """
Standard SAK EMKM Accounting Engine & Financial Statements for Odoo 18 Community Edition.
- SAK EMKM (Standar Akuntansi Keuangan Entitas Mikro, Kecil, dan Menengah) Chart of Accounts
- Native Financial Reports for Community Edition (Zero Enterprise Dependencies):
  * Laporan Laba Rugi (Income Statement / Profit & Loss)
  * Laporan Posisi Keuangan (Neraca / Balance Sheet)
  * Laporan Arus Kas (Cash Flow Statement - Direct Method)
- Indonesian Tax Accounting Integration:
  * PPN Keluaran & PPN Masukan 12% (UU HPP No. 7/2021)
  * PPh 21 Karyawan & Bukan Pegawai
  * PPh 23 Jasa & Sewa
  * PPh Final UMKM 0.5% (PP 55/2022)
- One-Click PDF and Interactive Financial Statement Viewers
- Zero External Server Overhead - 100% Odoo 18 Community Native
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': ['account', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'data/account_sak_emkm_data.xml',
        'views/financial_report_views.xml',
        'views/account_account_views.xml',
        'views/accounting_menu_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

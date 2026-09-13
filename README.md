# Indonesia SAK EMKM Accounting & Financial Reports

[![Odoo](https://img.shields.io/badge/Odoo-18.0-714B67.svg)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-0f766e.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-AIRIV-0891b2.svg)](https://airiv.id)
[![GitHub Actions](https://github.com/arivonto/airiv_accounting_indonesia/actions/workflows/odoo-appstore-ci.yml/badge.svg?branch=18.0)](https://github.com/arivonto/airiv_accounting_indonesia/actions)
[![Apps Store Ready](https://img.shields.io/badge/Odoo%20Apps%20Store-ready-22c55e.svg)](https://apps.odoo.com/)

AIRIV Accounting Indonesia is an Odoo 18 Community accounting report layer for Indonesian SAK EMKM workflows. It adds SAK EMKM account classification, financial report records, calculated Laba Rugi and Neraca line generation from posted Odoo move lines, and a PPh Final UMKM 0.5% tax fixture.

## Core Capabilities & Architecture

### Core capabilities

- SAK EMKM account classification on `account.account`.
- Financial report workspace for Laba Rugi, Neraca, and Arus Kas option surface.
- Report calculation from posted Odoo accounting move lines.
- Laba Rugi sections: Pendapatan, HPP, Beban Operasional, and Laba Bersih.
- Neraca sections: Aset, Liabilitas, Ekuitas, and balance check.
- PPh Final UMKM 0.5% tax fixture based on PP 55/2022.

### Architecture

```text
Odoo Accounting Ledger
  |
  |-- account.account
  |-- account.move
  |-- account.move.line
  v
AIRIV SAK EMKM Classification
  |
  |-- l10n_id_emkm_category
  |-- PPh Final UMKM tax fixture
  v
Financial Report Engine
  |
  |-- airiv.financial.report
  |-- airiv.financial.report.line
  |-- Laba Rugi
  |-- Neraca
  v
Management Review
  |
  |-- total pendapatan
  |-- HPP and operating expense
  |-- laba bersih
  |-- asset, liability, equity
  |-- balance check
```

## Feature & Workflow Automation

1. Prepare accounts
   - Review chart of accounts and fill SAK EMKM category mapping where needed.

2. Post accounting entries
   - Use standard Odoo accounting documents and post journal entries, invoices, or bills.

3. Calculate financial report
   - Create a financial report, select report type, date range, and company, then click `Hitung Saldo Laporan`.

4. Review management totals
   - Review revenue, HPP, operating expenses, net income, assets, liabilities, equity, and balance difference.

## Technical Specifications

| Item | Detail |
| --- | --- |
| Odoo series | 18.0 |
| Odoo edition | Community |
| Module technical name | `airiv_accounting_indonesia` |
| Version | `18.0.1.0.0` |
| License | LGPL-3 |
| Author | AIRIV |
| Category | Accounting/Localizations/Account Charts |
| Dependencies | `account`, `base` |
| Main models | `account.account`, `airiv.financial.report`, `airiv.financial.report.line` |
| Report types | `laba_rugi`, `neraca`, `arus_kas` |
| Report sections | `pendapatan`, `hpp`, `beban_ops`, `aset`, `liabilitas`, `ekuitas` |
| Tax fixture | PPh Final UMKM 0.5% PP 55/2022 |
| Store assets | `icon.png`, `banner.png`, `index.html` |

## Installation Guidance

1. Clone the repository branch for Odoo 18:

   ```bash
   git clone -b 18.0 https://github.com/arivonto/airiv_accounting_indonesia.git
   ```

2. Place the module in your Odoo addons path.

3. Restart Odoo.

4. Activate developer mode if needed.

5. Update the Apps list.

6. Search for `Indonesia SAK EMKM Accounting & Financial Reports`.

7. Install the module.

## Configuration Checklist

- Confirm Odoo Accounting is installed.
- Review account types and chart of accounts before report generation.
- Fill SAK EMKM category values on accounts where useful.
- Confirm PPh Final UMKM 0.5% tax fixture is available after installation.
- Post accounting entries before calculating reports.
- Set date range carefully for Laba Rugi reports.
- For Neraca, review asset, liability, equity, and balance check values.

## Repository Layout

```text
airiv_accounting_indonesia/
  README.md
  LICENSE
  .github/
    workflows/
      odoo-appstore-ci.yml
    scripts/
      validate_odoo_appstore.py
  airiv_accounting_indonesia/
    __manifest__.py
    data/
      account_sak_emkm_data.xml
    models/
      account_account.py
      financial_report.py
    security/
      ir.model.access.csv
    static/
      description/
        icon.png
        icon_128.png
        airiv_store_icon.png
        airiv_store_icon_128.png
        banner.png
        index.html
    views/
      account_account_views.xml
      accounting_menu_views.xml
      financial_report_views.xml
  static/
    description/
      icon.png
      icon_128.png
      airiv_store_icon.png
      airiv_store_icon_128.png
      banner.png
      index.html
```

## Contact Info

| Item | Detail |
| --- | --- |
| Author | AIRIV |
| Website | https://airiv.id |
| GitHub | https://github.com/arivonto |
| Module repository | https://github.com/arivonto/airiv_accounting_indonesia |
| Odoo series | 18.0 |

## Quality Gate

This repository is prepared for Odoo Apps Store submission with:

- Parseable Odoo manifest metadata.
- Root and module-level documentation.
- Odoo Apps Store description fragment.
- Required store images.
- LGPL-3 license metadata.
- GitHub Actions Apps Store audit on branch `18.0`.


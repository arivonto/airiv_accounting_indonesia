# Indonesia SAK EMKM Accounting & Financial Reports (Neraca & Laba Rugi)

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Accounting: SAK EMKM](https://img.shields.io/badge/Standard-SAK%20EMKM%20IAI-blue.svg)](https://airiv.id)

A complete, standalone Indonesian Accounting & Financial Reporting engine designed specifically for **Odoo 18.0 Community Edition**. Provides native financial statements (**Laporan Laba Rugi**, **Laporan Posisi Keuangan / Neraca**) under **SAK EMKM** standards without requiring Odoo Enterprise `account_reports`.

---

## Detailed Capabilities

### 1. SAK EMKM Chart of Accounts (Standar IAI)
* Standard account classifications specifically curated for Indonesian micro, small, and medium businesses (UMKM).
* Pre-configured tax accounts for PPN 12% (Keluaran & Masukan), PPh 21, PPh 23, and PPh Final UMKM 0.5% (PP 55/2022).

### 2. Native Financial Statement Generator (Zero Enterprise Dependencies)
* **Laporan Laba Rugi (Income Statement)**: Calculates Total Pendapatan Usaha, Beban Pokok Penjualan (HPP), Laba Kotor, Beban Operasional, and Laba/Rugi Bersih.
* **Laporan Posisi Keuangan (Neraca)**: Real-time balance consolidation of Aset Lancar, Aset Tetap, Liabilitas Jangka Pendek/Panjang, and Ekuitas with automated balance checking.
* **Interactive Summary Dashboard**: High-level KPI summary cards embedded directly into the financial report viewer.

---

## Validated Commercial Test Benchmark (Scrutinized)

The accounting engine was verified under live Odoo 18.0 Community conditions:

1. **Tax Standard Verification**: Validated statutory **PPh Final UMKM 0.5% (PP 55/2022)** sales tax rule fixture.
2. **Laporan Laba Rugi Engine**: Computed revenue aggregation totaling **Rp 340.743,57** with complete ledger line mapping across active nominal accounts.
3. **Laporan Posisi Keuangan (Neraca)**: Consolidated real-time assets totaling **Rp 340.743,57** with multi-account mapping into standard SAK EMKM asset classifications.

---

## Installation & Odoo Configuration Guide

1. **Deploy Module**:
   Place `airiv_accounting_indonesia` inside your Odoo `custom_addons` directory.

2. **Activate Module**:
   * Navigate to **Apps > Update Apps List**.
   * Search for `Indonesia SAK EMKM Accounting & Financial Reports` and click **Activate**.

3. **Generate Financial Statements**:
   * Open **Invoicing / Accounting > Reporting > Laporan SAK EMKM**.
   * Select **Laporan Laba Rugi** or **Posisi Keuangan (Neraca)**.
   * Choose your fiscal date range and click **Hitung Saldo Laporan** to populate account totals.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL & App Drawer compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `account`, `base` |
| **Server Overhead** | Zero (Native ORM, direct SQL ledger aggregations) |
| **Accounting Standard** | SAK EMKM (Ikatan Akuntan Indonesia), PP 55/2022, UU HPP No. 7/2021 |

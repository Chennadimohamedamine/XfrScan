# 🛡️ XfrScan Zone Transfer Check Tool

A simple Python script to check if any nameservers for a given domain allow **DNS zone transfer (AXFR)** — a common DNS misconfiguration that can leak sensitive information.

## 🚀 Features

- Automatically resolves nameservers (`NS`) for a domain
- Attempts AXFR (Zone Transfer) from each
- Reports if any name server is vulnerable

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/zone-transfer-check.git
cd zone-transfer-check
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
## 🧪 Usage

```bash
python3 zone_transfer_check.py example.com
```

## © Copyright

© 2025 [mohamed amine]
All rights reserved.
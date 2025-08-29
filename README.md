# 🛡️ XfrScan Zone Transfer Check Tool

A simple Python script to check if any nameservers for a given domain allow **DNS zone transfer (AXFR)** — a common DNS misconfiguration that can leak sensitive information.

## 🚀 Features

- Automatically resolves nameservers (`NS`) for a domain
- Attempts AXFR (Zone Transfer) from each
- Reports if any name server is vulnerable

## 🔧 Installation

### 1. Clone the repository

```bash
git clone git@github.com:Chennadimohamedamine/XfrScan.git
cd XfrScan
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
## 🧪 Usage

### Single Domain
```bash
python3 XfrScan.py -d example.com
```
### Multiple Domains from File
```
python3 XfrScan.py -dl list.txt
```
### Show Help
```
python3 XfrScan.py -h
```
### Show Version
```
python3 XfrScan.py -v
```
## Example Output
```
=== Testing zonetransfer.me ===
[!!] Zone transfer successful on zonetransfer.me -> nsztm1.digi.ninja (81.4.108.41)

_acme-challenge.zonetransfer.me. 7200 IN TXT "abc123"
...

=== Testing example.com ===
[+] No name servers allow zone transfer for example.com. Looks good.

```

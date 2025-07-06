# Cybersecurity-mini-project
All Project code in python simple and easy to understand.

# 🛡️ Phishing URL Detector

A lightweight Python script to detect potentially **phishing URLs** using simple heuristic rules.

---

## 🔍 Features

- ✅ URL format validation  
- ⚠️ Heuristic-based detection rules:
  - Contains `@` symbol
  - Length > 75 characters
  - IP address used in domain
  - Suspicious keywords like `login`, `verify`, `bank`, etc.
  - Too many hyphens
  - Suspicious top-level domains (e.g. `.xyz`, `.zip`) *(optional)*

---

## 📁 Example

```bash
$ python phishing_check.py https://secure-login.bank.example.com

🔍 Analyzing: https://secure-login.bank.example.com
⚠️  Contains @
⚠️  Length Gt 75
⚠️  Suspicious Keyword
⚠️  Too Many Hyphens

Result: 🚨  Likely Phishing (contains_@, length_gt_75, suspicious_keyword, too_many_hyphens)

--------------------------------------------------------------------------------------------------------------------------

# ⌨️ Simple Python Keylogger

This is a **minimal keylogger** built in Python using the `pynput` library. It records every key press along with the timestamp and saves it to a file named `keylog.txt`.

> ⚠️ **DISCLAIMER:**  
> This tool is for **educational and authorized use only**. Unauthorized use of keyloggers may be **illegal** and unethical. Always get explicit permission before running this script on any system.

---

## 📌 Features

- Logs every key press (printable and special keys)
- Timestamps each keystroke
- Saves logs to a file (`keylog.txt`)
- Press `Esc` to stop the logger safely
- Works on **Windows**, **Linux**, and **macOS**

### Install Required Package

```bash
pip install pynput
--------------------------------------------------------------------------------------------------------------------------
# 🔎 Simple Python Port Scanner

A lightweight Python script to scan the first 1024 TCP ports on any IP address or domain.

> ⚠️ **Note:** Use this tool only on systems you own or have explicit permission to test. Unauthorized scanning may be illegal.

---

## 🚀 How to Use

### 1. Install Python (3.x)

### 2. Run the script

```bash
python port_scanner.py

## What It Does
Scans ports 1 to 1024 using socket

Reports all open ports

Displays total scan time

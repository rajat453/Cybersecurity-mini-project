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

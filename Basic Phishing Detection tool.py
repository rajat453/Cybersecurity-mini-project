import re
import validators

def is_phishing(url):
    # Validate URL format
    if not validators.url(url):
        return "❌ Invalid URL format"

    # Heuristic rules
    rules = {
        "Contains @ symbol": '@' in url,
        "Too long (>75 chars)": len(url) > 75,
        "IP address in domain": bool(re.search(r"http[s]?://\d{1,3}(\.\d{1,3}){3}", url)),
        "Suspicious keywords": any(word in url.lower() for word in ['login', 'verify', 'update', 'secure', 'bank']),
        "Too many hyphens": url.count('-') > 3
    }

    print(f"\n🔍 Analyzing: {url}")
    suspicious = False
    for rule, matched in rules.items():
        if matched:
            suspicious = True
            print(f"⚠️  Rule matched: {rule}")

    return "🚨 Likely Phishing" if suspicious else "✅ Looks Safe"

# --------- Run on user input ---------
url_input = input("Enter a URL to scan: ")
result = is_phishing(url_input)
print("\nResult:", result)

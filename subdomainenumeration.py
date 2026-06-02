import requests

def enumeration(domain, wordlist):
    found = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    for sub in wordlist:
        sub = sub.strip()
        if not sub:  
            continue

        url = f"https://{sub}.{domain}"
        try:
            requests.get(url, headers=headers, timeout=3)
            print(f"[*] Found : {url}")
            found.append(url)
        except requests.ConnectionError:
            pass
        except requests.Timeout:
            pass
    return found



subdomains = [
    "www",
    "mail",
    "remote",
    "blog",
    "webmail",
    "server",
    "ns1",
    "ns2",
    "smtp",
    "secure",
    "vpn",
    "api",
    "dev",
    "ftp",
    "m",
    "shop",
    "admin",
    "portal",
    "test",
    "support",
    "status",
    "static",
    "demo",
    "app",
    "cloud",
    "stage",
    "internal",
    "localhost",
    "exchange",
    "git",
    "gitlab",
    "jenkins",
    "jira",
    "wiki",
    "monitor",
    "mysql",
    "db",
    "dashboard",
    "assets",
    "billing",
    "images",
    "media",
    "cdn",
    "download",
    "help",
    "login",
    "auth",
    "panel",
    "en",
    "office",
]

domain = input("Enter the domain you want to search for : ")
enumeration(domain, subdomains)

print('_' * 100)

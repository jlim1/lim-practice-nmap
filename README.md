# Read a saved port inventory

Reads `sample.xml` and prints only the open service: `192.0.2.10 tcp 443 https`.

From the repository root with Python 3.10 or newer (standard library only):

```sh
python review_report.py
```

Keep the XML next to the script. This offline example does not scan a network or require Nmap.

# fchk.py
Facebook ID Checker 🔍
Developer: Mueid Mursalin Rifat
Version: 2.0

A Python tool for checking Facebook account credentials with multi-threading support.

✨ Features

· Multi-threading for fast checking
· Real-time progress tracking
· Automatic account classification (OK/CP/Failed)
· Session cookie extraction
· Colorful terminal interface
· Results export to files

🚀 Quick Start

1. Install requirements:

```bash
pip install requests
```

1. Prepare accounts file (uid|password format):

```
123456789|password123
987654321|mypass456
```

1. Run the tool:

```bash
cd fchk
python fchk.py
```

📁 Output Files

· OK_ACCOUNTS.txt - Working accounts
· CP_ACCOUNTS.txt - Checkpoint accounts
· COOKIES.txt - Session cookies

⚠️ Disclaimer

For educational purposes only. Use only on accounts you own.


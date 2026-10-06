# AUTOBOT v2.0

AUTOBOT v2.0 is a modular security automation framework designed for efficiency, anonymity, and custom workflow orchestration. It combines a modern Python-based TUI with powerful Bash execution modules to streamline security auditing and penetration testing.

# Key Features

#  Hybrid Architecture
- **Python Brain**: A `rich`-powered terminal user interface (TUI) for easy navigation and management.
- **Bash Execution**: Specialized modules for different security domains, ensuring raw performance and direct tool integration.

# Smart Action System (Custom Workflows)
The standout feature of AUTOBOT v2.0 is the ability to record and parameterize your own workflows:
1. **Record**: Enter a sequence of commands.
2. **Parameterize**: Define specific strings (like IP addresses or flags) as variables.
3. **Execute**: Run the workflow and be prompted to replace those variables in real-time, or press Enter to use the defaults.

# Intelligent Tool Database
- **Integrated Database**: A curated list of tools categorized by function.
- **Smart Install**: If a tool isn't installed, AUTOBOT attempts to install it via `apt`. If that fails, it provides guidance for manual GitHub installation.

# Module Overview

- **Anonymity & Privacy**: MAC spoofing (with revert), Anonsurf (Start/Stop), and Proxychains management.
- **Wireless Security**: Aircrack-ng, Sparrow-WiFi, and advanced wireless auditing.
- **Web Security**: SQLMap and DirBuster for vulnerability scanning and directory brute-forcing.
- **Network & MITM**: Nmap (with service versioning), Bettercap, and mitm6.
- **Exploitation Framework**: Direct integration with Metasploit and MSFVenom.

# Installation

# Prerequisites
- Python 3.x
- Kali Linux (Recommended)
- Required Python Library: `rich`

# Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/aviator899/autobot.git
   cd autobot
   ```
2. Run the installation script:
   ```bash
   chmod +x install.sh
   sudo ./install.sh
   ```
3. Launch the tool:
   ```bash
   python main.py
   ```

# Terminal Fix
If you use tools like Metasploit and exit using `Ctrl+C`, your terminal may behave strangely (e.g., showing `^M` when you press Enter). To fix this, simply run:
```bash
reset
# or
stty sane
```

---

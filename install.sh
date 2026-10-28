#!/bin/bash

# Autobot v2 Installation Script
echo -e "\e[1;34m[+]\e[0m Initializing AUTOBOT v2.0 Installation..."

# Check if root
if [ "$EUID" -ne 0 ]; then
  echo -e "\e[1;31m[!] Please run as root (sudo ./install.sh)\e[0m"
  exit
fi

# Update system
echo -e "\e[1;33m[*] Updating package lists...\e[0m"
apt-get update -y

# Install Python dependencies
echo -e "\e[1;33m[*] Installing Python dependencies...\e[0m"
apt-get install -y python3-pip
pip3 install rich

# Create necessary directories
mkdir -p logs custom config

echo -e "\n\e[1;32m[+] AUTOBOT v2.0 Installation Complete!\e[0m"
echo -e "To start the framework: python3 autobot.py"

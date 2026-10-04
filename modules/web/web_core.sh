#!/bin/bash

# Autobot v2 Web Security Module
# This script is called by the Python Core Engine

YELLOW='\033[1;33m'
RED='\033[1;31m'
GREEN='\033[0;32m'
NC='\033[0m'

function banner() {
    clear
    echo -e "${YELLOW}==================================================${NC}"
    echo -e "${YELLOW}       AUTOBOT v2 - WEB SECURITY               ${NC}"
    echo -e "${YELLOW}==================================================${NC}"
}

function sql_injection() {
    echo -e "\n${YELLOW}[*] SQL Injection (SQLMap)${NC}"
    read -p "Enter target URL: " URL
    if [[ -z "$URL" ]]; then return; fi

    echo -e "1) Basic Scan"
    echo -e "2) Full Database Dump"
    read -p "Choice: " MODE

    if [[ "$MODE" == "1" ]]; then
        sqlmap -u "$URL" --batch
    elif [[ "$MODE" == "2" ]]; then
        sqlmap -u "$URL" --batch --dbs
    else
        echo -e "${RED}[!] Invalid choice${NC}"
    fi
}

function launch_dirbuster() {
    echo -e "\n${YELLOW}[*] Launching DirBuster...${NC}"
    if command -v dirbuster &> /dev/null; then
        dirbuster
    else
        echo -e "${RED}[!] DirBuster not found. Please install it via apt or GitHub.${NC}"
    fi
}

function xss_check() {
    echo -e "\n${YELLOW}[*] XSS Vulnerability Check${NC}"
    read -p "Enter target URL: " URL
    if [[ -z "$URL" ]]; then return; fi

    echo -e "${YELLOW}[*] Checking for common XSS vectors...${NC}"
    curl -s "$URL?q=<script>alert(1)</script>" | grep -i "alert(1)" && echo -e "${GREEN}[+] Potential XSS found!${NC}" || echo -e "${RED}[-] No simple XSS found${NC}"
}

banner
echo -e "1) SQL Injection (SQLMap)"
echo -e "2) DirBuster"
echo -e "3) XSS Scanner"
echo -e "0) Return to Main Menu"
echo -e "\nChoose an option:"
read OPT

case $OPT in
    1) sql_injection ;;
    2) launch_dirbuster ;;
    3) xss_check ;;
    *) echo -e "Returning..." ;;
esac

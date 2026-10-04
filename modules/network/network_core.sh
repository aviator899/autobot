#!/bin/bash

# Autobot v2 Network & MITM Module
# This script is called by the Python Core Engine

YELLOW='\033[1;33m'
RED='\033[1;31m'
GREEN='\033[0;32m'
NC='\033[0m'

function banner() {
    clear
    echo -e "${YELLOW}==================================================${NC}"
    echo -e "${YELLOW}       AUTOBOT v2 - NETWORK & MITM               ${NC}"
    echo -e "${YELLOW}==================================================${NC}"
}

function network_scan() {
    echo -e "\n${YELLOW}[*] Network Scanning (Service Versioning)${NC}"
    read -p "Enter Target IP/Range (e.g., 192.168.1.0/24): " TARGET
    if [[ -z "$TARGET" ]]; then return; fi

    echo -e "${YELLOW}[*] Scanning $TARGET with nmap -sV...${NC}"
    nmap -sV $TARGET
}

function mitm_setup() {
    echo -e "\n${YELLOW}[*] MITM Infrastructure Setup${NC}"
    echo "1) Enable IP Forwarding"
    echo "2) Disable IP Forwarding"
    read -p "Choice: " MODE

    if [[ "$MODE" == "1" ]]; then
        echo 1 > /proc/sys/net/ipv4/ip_forward
        echo -e "${GREEN}[+] IP Forwarding Enabled${NC}"
    elif [[ "$MODE" == "2" ]]; then
        echo 0 > /proc/sys/net/ipv4/ip_forward
        echo -e "${GREEN}[+] IP Forwarding Disabled${NC}"
    fi
}

function arp_spoof() {
    echo -e "\n${YELLOW}[*] ARP Spoofing (Bettercap)${NC}"
    if command -v bettercap &> /dev/null; then
        echo -e "${YELLOW}[*] Launching Bettercap...${NC}"
        bettercap
    else
        echo -e "${RED}[!] Bettercap not found. Install with 'apt install bettercap'${NC}"
    fi
}

function launch_mitm6() {
    echo -e "\n${YELLOW}[*] Launching mitm6...${NC}"
    if command -v mitm6 &> /dev/null; then
        mitm6
    else
        echo -e "${RED}[!] mitm6 not found. Install with 'apt install mitm6'${NC}"
    fi
}

banner
echo -e "1) Fast Network Scan (sV)"
echo -e "2) MITM IP Forwarding"
echo -e "3) Launch Bettercap (MITM)"
echo -e "4) Launch mitm6 (IPv6 MITM)"
echo -e "0) Return to Main Menu"
echo -e "\nChoose an option:"
read OPT

case $OPT in
    1) network_scan ;;
    2) mitm_setup ;;
    3) arp_spoof ;;
    4) launch_mitm6 ;;
    *) echo -e "Returning..." ;;
esac

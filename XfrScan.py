#!/usr/bin/env python3
import dns.resolver
import dns.query
import dns.zone
import socket
import sys
import argparse

def GetNameServers(domain):
    """Fetch NS records for the domain"""
    try:
        ns = dns.resolver.resolve(domain, 'NS')
        return [str(n.target).rstrip('.') for n in ns]
    except Exception:
        return []

def CheckZoneTransfer(domain, ns):
    """Attempt a zone transfer from the given NS"""
    try:
        ip = socket.gethostbyname(ns)  # Resolve hostname to IPv4
        zone = dns.zone.from_xfr(dns.query.xfr(ip, domain, timeout=5))
        if zone:
            print(f"\n[!!] Zone transfer successful on {domain} -> {ns} ({ip})\n")
            for name, node in zone.nodes.items():
                print(zone[name].to_text(name))
            return True
    except Exception as e:
        print(f"[-] Zone transfer failed on {domain} -> {ns}: {e}")
        return False
    return False

def ProcessDomain(domain):
    """Process a single domain"""
    print(f"\n=== Testing {domain} ===")
    nameservers = GetNameServers(domain)
    if not nameservers:
        print(f"[!] No NS records found for {domain}.")
        return

    vulnerable = False
    for ns in nameservers:
        if CheckZoneTransfer(domain, ns):
            vulnerable = True

    if not vulnerable:
        print(f"[+] No name servers allow zone transfer for {domain}. Looks good.")

def main():
    parser = argparse.ArgumentParser(
        description="DNS Zone Transfer Checker Tool",
        usage=(
            "python3 %(prog)s -d <domain>\n"
            "python3 %(prog)s -dl <listfile>\n"
            "python3 %(prog)s -h"
        )
    )
    parser.add_argument(
        "-d", "--domain",
        help="Target domain to test for zone transfer"
    )
    parser.add_argument(
        "-dl", "--domain-list",
        help="File containing list of domains to test"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="ZoneTransfer Tool v2.0"
    )

    args = parser.parse_args()

    if not args.domain and not args.domain_list:
        parser.print_help()
        sys.exit(1)

    # Single domain mode
    if args.domain:
        ProcessDomain(args.domain)

    # Multiple domains mode
    if args.domain_list:
        try:
            with open(args.domain_list, 'r') as f:
                domains = [line.strip() for line in f if line.strip()]
            for domain in domains:
                ProcessDomain(domain)
        except FileNotFoundError:
            print(f"[!] File '{args.domain_list}' not found.")
            sys.exit(1)

if __name__ == "__main__":
    main()


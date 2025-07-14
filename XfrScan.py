import dns.resolver
import dns.query
import dns.zone
import sys

def GetNameServers(domain):
    try:
        ns = dns.resolver.resolve(domain, 'NS')
        return [str(n.target).rstrip('.') for n in ns]
    except Exception as e:
        return []

def CheckZoneTransfer(domain, ns):
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(ns, domain, timeout=5))
        if zone:
            print(f"[!!] Zone transfer successful on {ns}!\n")
            for name, node in zone.nodes.items():
                print(zone[name].to_text(name))
            return True
    except Exception as e:
        return False
    return False

def main(domain):
    nameservers = GetNameServers(domain)
    if not nameservers:
        print("[!] No NS records found.")
        return

    vulnerable = False
    for ns in nameservers:
        if CheckZoneTransfer(domain, ns):
            vulnerable = True
            break

    if not vulnerable:
        print("[+] No name servers allow zone transfer. Looks good.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <domain>")
        sys.exit(1)
    main(sys.argv[1])

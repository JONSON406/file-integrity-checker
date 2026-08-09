import socket


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))
        sock.close()

        return result == 0

    except socket.error:
        return False


def port_scanner(target, start_port, end_port):
    print(f"\n[*] Scanning {target}")
    print(f"[*] Ports: {start_port}-{end_port}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

    print("\n[*] Scan completed.")

    if not open_ports:
        print("[-] No open ports found.")

    return open_ports
from port_scanner import port_scanner
from banner_grabber import grab_banner


def main():
    print("=" * 50)
    print("       PENETRATION TESTING TOOLKIT")
    print("=" * 50)

    target = input("\nEnter target IP/hostname: ").strip()

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range.")
            return

    except ValueError:
        print("Please enter valid port numbers.")
        return

    open_ports = port_scanner(target, start_port, end_port)

    print("\n[*] Attempting banner detection...")

    for port in open_ports:
        banner = grab_banner(target, port)

        print(f"\nPort {port}:")
        print(banner if banner else "No banner detected.")

    print("\n[*] Toolkit execution completed.")


if __name__ == "__main__":
    main()
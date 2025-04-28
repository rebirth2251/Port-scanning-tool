import socket
import sys

def scan_ports(ip, start_port, end_port):
    open_ports = []

    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Short timeout
            result = sock.connect_ex((ip, port))  # 0 = success
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user. Exiting...")
            sys.exit()
        except socket.gaierror:
            print("[!] Hostname could not be resolved. Exiting...")
            sys.exit()
        except socket.error:
            print("[!] Could not connect to server. Exiting...")
            sys.exit()
    
    if not open_ports:
        print("\n[-] No open ports found.")
    else:
        print(f"\n[+] Open ports: {open_ports}")

def get_valid_ip():
    while True:
        ip = input("Enter target IP address: ").strip()
        try:
            socket.inet_aton(ip)  # Validate IP
            return ip
        except socket.error:
            print("[!] Invalid IP address format. Try again.")

def get_valid_port(prompt):
    while True:
        try:
            port = int(input(prompt))
            if 0 <= port <= 65535:
                return port
            else:
                print("[!] Port must be between 0 and 65535.")
        except ValueError:
            print("[!] Please enter a valid integer.")

if __name__ == "__main__":
    print("== Basic Port Scanner ==")
    target_ip = get_valid_ip()
    start_port = get_valid_port("Enter start port: ")
    end_port = get_valid_port("Enter end port: ")

    if start_port > end_port:
        print("[!] Start port must be less than or equal to end port.")
        sys.exit()

    scan_ports(target_ip, start_port, end_port)

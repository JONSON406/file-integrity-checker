
import socket


def grab_banner(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        sock.connect((target, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")

        banner = sock.recv(1024).decode(errors="ignore")
        sock.close()

        return banner.strip()

    except Exception:
        return "Unable to retrieve banner."
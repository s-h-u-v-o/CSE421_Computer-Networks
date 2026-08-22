import socket

host_ip = '127.0.0.1'
port = 50001


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host_ip, port))
    server.listen(5)
    print(f"Server is listening...")

    conn, addr = server.accept()
    print(f"Connected to client:")

    client_ip, device_name = conn.recv(512).decode().split(',')

    print(f"Client IP: {client_ip}")
    print(f"Device Name: {device_name}")

    conn.close()
    server.close()


if __name__ == "__main__":
    main()

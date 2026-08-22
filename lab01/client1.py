import socket

s_ip = '127.0.0.1'
s_port = 50001


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((s_ip, s_port))

    # Get this machine's IP address and device (host) name
    device_name = socket.gethostname()
    client_ip = socket.gethostbyname(device_name)

    message = f"{client_ip},{device_name}"
    client.send(message.encode())

    client.close()


if __name__ == "__main__":
    main()

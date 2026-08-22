import socket

s_ip = '127.0.0.1'
s_port = 50001


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((s_ip, s_port))

    message = input("Enter a message to send to server: ")
    client.send(message.encode())

    response = client.recv(512).decode()
    print(f"Server response: {response}")

    client.close()


if __name__ == "__main__":
    main()

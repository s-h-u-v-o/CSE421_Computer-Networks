import socket

host_ip = '127.0.0.1'
port = 50001
vwls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def count_vowels(text):
    return sum(1 for ch in text if ch in vwls)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host_ip, port))
    server.listen(5)
    print(f"Server is listening...")

    conn, addr = server.accept()
    print(f"Connected to client:")

    data = conn.recv(512).decode()
    print(f"Received message: {data}")

    vowel_count = count_vowels(data)
    print(f"Vowel count: {vowel_count}")

    if vowel_count == 0:
        response = "Not enough vowels"
    elif vowel_count <= 2:
        response = "Enough vowels I guess"
    else:
        response = "Too many vowels"

    conn.send(response.encode())
    conn.close()
    server.close()


if __name__ == "__main__":
    main()

import socket
import threading

host_ip = '127.0.0.1'
port = 50001
vwls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 1


def count_vowels(text):
    return sum(1 for ch in text if ch in vwls)


def handle_client(conn, addr, count):
    print(f"Client {count} Connected")
    try:
        data = conn.recv(512).decode()
        print(f"Client {count}'s Received message: {data}")

        vowel_count = count_vowels(data)
        print(f"Client {count}'s Vowel count: {vowel_count}")

        if vowel_count == 0:
            response = "Not enough vowels"
        elif vowel_count <= 2:
            response = "Enough vowels I guess"
        else:
            response = "Too many vowels"

        conn.send(response.encode())
    finally:
        conn.close()
        print(f"Client {count}'s Connection closed")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host_ip, port))
    server.listen(5)
    print(f"Multi-threaded server is listening...")
    
    global count

    while True:
        print(f"Active client threads: {threading.active_count() - 1}")
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, count))
        thread.start()
        count += 1


if __name__ == "__main__":
    main()

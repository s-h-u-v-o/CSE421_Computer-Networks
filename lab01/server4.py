import socket

host_ip = '127.0.0.1'
port = 50001


def calculate_salary(hours):
    if hours <= 40:
        return hours * 200
    else:
        return 8000 + (hours - 40) * 300


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host_ip, port))
    server.listen(5)
    print(f"Server is listening...")

    conn, addr = server.accept()
    print(f"Connected to client:")

    data = conn.recv(512).decode()
    hours = float(data)
    print(f"Hours worked received: {hours}")

    salary = calculate_salary(hours)
    response = f"Salary: Tk {salary:.2f}"
    print(response)

    conn.send(response.encode())
    conn.close()
    server.close()


if __name__ == "__main__":
    main()

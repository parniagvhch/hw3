import socket

def calculate(cal, op1, op2):
    if cal == "add":
        return op1 + op2
    elif cal == "sub":
        return op1 - op2
    elif cal == "mul":
        return op1 * op2
    elif cal == "div":
        if op2 != 0:
            return op1 / op2
        else:
            return "error in op2"

def func():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('127.0.0.1',1234))
    server.listen(3)
    print("Server is listening for incoming connections...")

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")

        while True:
            data = client.recv(1024).decode()
            if not data:
                continue


            operation = data.split(" ")
            cal=operation[0]
            op1 = float(operation[1])
            op2 = float(operation[2])


            result = calculate(cal, op1, op2)
            client.send(str(result).encode())

        client.close()

if __name__ == "__main__":
    func()



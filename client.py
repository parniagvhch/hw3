import socket

def func():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 1234))
    except ConnectionRefusedError:
        print("Connection to the server failed")
        return

    while True:
        operation = input("write operations eg:(add 5 8) or exit if you want to stop: ")
        # inputs.append((operation))


        if operation == "exit":
            break

        a = f"{operation}"
        client.send(a.encode())
        result = client.recv(1024).decode()
        print(f"Result: {result}")

    client.close()

if __name__ == "__main__":
    func()

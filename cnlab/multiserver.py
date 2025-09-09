import socket
import threading

def handle_client(client_socket, addr, server_name, server_integer):
    try:
        data = client_socket.recv(1024).decode()
        if not data:
            return

        client_name, client_num = data.split("|")
        client_num = int(client_num)

        if not (1 <= client_num <= 100):
            print("[SERVER] Invalid number received. Closing.")
            client_socket.close()
            return

        total = client_num + server_integer

        # Display on server side
        print("\n=== Transaction on Server ===")
        print(f"Client Name: {client_name}")
        print(f"Server Name: {server_name}")
        print(f"Client Integer: {client_num}")
        print(f"Server Integer: {server_integer}")
        print(f"Sum: {total}")
        print("=============================\n")

        # Send reply
        reply = f"{server_name}|{server_integer}"
        client_socket.send(reply.encode())

    finally:
        client_socket.close()


def run_server(host="0.0.0.0", port=6000):
    server_name = "Server of John Q. Smith"
    server_integer = 42

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[SERVER] {server_name} listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[SERVER] Connection from {addr}")

        # Start a thread for each client
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, addr, server_name, server_integer)
        )
        thread.start()


if __name__ == "__main__":
    run_server()

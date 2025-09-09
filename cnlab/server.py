import socket

def run_server(host="0.0.0.0", port=7000):
    server_name = "Server of Rahul"
    server_integer = 42 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[SERVER] {server_name} listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[SERVER] Connected to client {addr}")

        # Receive data
        data = client_socket.recv(1024).decode()
        if not data:
            client_socket.close()
            continue

        
        try:
            client_name, client_num = data.split("|")
            client_num = int(client_num)
        except:
            print("[SERVER] Invalid data format. Closing connection.")
            client_socket.close()
            continue

        if not (1 <= client_num <= 100):
            print("[SERVER] Invalid number received. Terminating server.")
            client_socket.close()
            server_socket.close()
            break

        total = client_num + server_integer

        # Display on server side
        print("\n=== Transaction on Server ===")
        print(f"Client Name: {client_name}")
        print(f"Server Name: {server_name}")
        print(f"Client Integer: {client_num}")
        print(f"Server Integer: {server_integer}")
        print(f"Sum: {total}")
        print("=============================\n")

        # Send reply back to client
        reply = f"{server_name}|{server_integer}"
        client_socket.send(reply.encode())

        client_socket.close()

if __name__ == "__main__":
    run_server()

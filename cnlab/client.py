import socket

def run_client(server_ip="127.0.0.1", port=7000):
    client_name = "Client of Rahul"

    
    try:
        client_num = int(input("Enter an integer (1–100): "))
    except ValueError:
        print("Invalid input. Must be an integer.")
        return

    if not (1 <= client_num <= 100):
        print("Number must be between 1 and 100.")
        return

    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip,port))

    # Send message: "ClientName|Integer"
    message = f"{client_name}|{client_num}"
    client_socket.send(message.encode())

    # Receive reply
    reply = client_socket.recv(1024).decode()
    server_name, server_num = reply.split("|")
    server_num = int(server_num)

    total = client_num + server_num

    # Display results on client side
    print("\n=== Transaction on Client ===")
    print(f"Client Name: {client_name}")
    print(f"Server Name: {server_name}")
    print(f"Client Integer: {client_num}")
    print(f"Server Integer: {server_num}")
    print(f"Sum: {total}")
    print("=============================\n")

    client_socket.close()

if __name__ == "__main__":
    run_client()

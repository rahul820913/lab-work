import socket

HOST = "127.0.0.1"
PORT = 8081

def handle_request(request):
    headers = request.split("\r\n")
    cookie = None

    for header in headers:
        if header.startswith("Cookie:"):
            cookie = header.split(":", 1)[1].strip()

    if cookie:
        body = f"<h1>Welcome back, {cookie}!</h1>"
    else:
        body = "<h1>Hello, new user! Cookie set.</h1>"
        cookie = "User123"

    response = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Content-Type: text/html\r\n"
        f"Set-Cookie: {cookie}\r\n"
        "\r\n"
        f"{body}"
    )
    return response.encode()

# Run server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server running on http://{HOST}:{PORT}")

    while True:
        client_conn, addr = server_socket.accept()
        with client_conn:
            request = client_conn.recv(1024).decode()
            if not request:
                continue
            response = handle_request(request)
            client_conn.sendall(response)

import socket

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on", (HOST, PORT))
    
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Client says:", data)
            
            if data == "stop":
                response = "Connection closed."
                conn.sendall(response.encode())
                break
            else:
                response = "Message received: " + data
                conn.sendall(response.encode())

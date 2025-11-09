import socket, os

IP, PORT = "0.0.0.0", 5001
BUF = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, PORT))

print("Server ready...")

while True:
    info, addr = s.recvfrom(BUF)
    try:
        name, size, ftype = info.decode().split("::")
        size = int(size)
    except:
        continue

    with open("recv_" + name, "wb") as f:
        recd = 0
        while recd < size:
            data, _ = s.recvfrom(BUF)
            f.write(data)
            recd += len(data)
    print(f"Received {ftype} file: {name}")

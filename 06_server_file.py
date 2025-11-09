import socket

host = "127.0.0.1"
port = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print('New file will be created...')
f = open('Myfile2.txt', 'w')  # text mode OK if you decode

while True:
    data, addr = sock.recvfrom(1024)
    text = data.decode("utf-8")
    print(f"[SERVER] Received: {text}")

    if text == "Now":
        # end of transmission marker
        break

    f.write(text)  # write the decoded data to file

print('File is successfully received!!!')
f.close()

# Read back file contents
with open('Myfile2.txt', 'r') as f:
    print("[SERVER] File contents:")
    print(f.read())  # <-- call read()

sock.close()
print('Connection closed!')

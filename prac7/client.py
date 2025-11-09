import socket, os

IP, PORT = "127.0.0.1", 5001
BUF = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

files = {
    "script": "script.py",
    "text": "file.txt",
    "audio": "song.mp3",
    "video": "video.mp4"
}

for ftype, fname in files.items():
    if not os.path.exists(fname):
        continue
    size = os.path.getsize(fname)
    s.sendto(f"{fname}::{size}::{ftype}".encode(), (IP, PORT))
    with open(fname, "rb") as f:
        while (data := f.read(BUF)):
            s.sendto(data, (IP, PORT))
    print(f"Sent {ftype} file: {fname}")

s.close()

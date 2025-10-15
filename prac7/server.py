import socket
import mimetypes
import os
import subprocess
import sys

SERVER_IP = "0.0.0.0"  # Accept connections on all interfaces
PORT = 5001
BUFFER_SIZE = 1024
SAVE_PATH = "received_"  # Prefix for saved files

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

print(f"[SERVER] Listening on port {PORT}...")

while True:
    # Receive file info: filename and size
    file_info, addr = sock.recvfrom(BUFFER_SIZE)
    try:
        file_name, file_size = file_info.decode().split("::")
    except ValueError:
        print("[SERVER] Invalid file info received. Skipping.")
        continue

    file_size = int(file_size)
    full_save_path = SAVE_PATH + file_name

    # Detect file type
    mime_type, _ = mimetypes.guess_type(file_name)
    if mime_type:
        file_category = mime_type.split("/")[0]
    else:
        ext = os.path.splitext(file_name)[1].lower()
        if ext in ['.py', '.sh', '.bat']:
            file_category = 'script'
        elif ext in ['.txt', '.log', '.csv']:
            file_category = 'text'
        else:
            file_category = 'unknown'

    print(f"\n[SERVER] Receiving {file_category.upper()} file: {file_name} "
          f"({file_size} bytes) from {addr}")

    # Receive the file
    received_bytes = 0
    with open(full_save_path, "wb") as f:
        while received_bytes < file_size:
            data, _ = sock.recvfrom(BUFFER_SIZE)
            f.write(data)
            received_bytes += len(data)

    print(f"[SERVER] {file_category.upper()} file '{file_name}' received and "
          f"saved as '{full_save_path}'.")

    # 🔹 Open/play files automatically
    try:
        if file_category in ["audio", "video"]:
            print(f"[SERVER] Playing {file_category} file: {full_save_path}")
            if sys.platform.startswith("win"):
                os.startfile(full_save_path)
            elif sys.platform.startswith("darwin"):
                subprocess.run(["open", full_save_path])
            else:
                subprocess.run(["xdg-open", full_save_path])
        elif file_category == "text":
            print(f"[SERVER] Opening text file in Notepad: {full_save_path}")
            if sys.platform.startswith("win"):
                subprocess.run(["notepad.exe", full_save_path])
            else:
                print("[SERVER] Text auto-open is supported only on Windows in this script.")
    except Exception as e:
        print(f"[SERVER] Could not open/play file automatically: {e}")

sock.close()

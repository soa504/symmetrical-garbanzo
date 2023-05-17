import socket

import threading

def send_message():

    # Menentukan alamat IP dan port untuk server

    server_ip = '127.0.0.1'

    server_port = 8000

    # Membuat socket TCP

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Menghubungkan socket ke server

    server_socket.connect((server_ip, server_port))

    # Menerima input dari pengguna dan mengirimkannya ke server

    while True:

        message = input("Pesan: ")

        server_socket.send(message.encode())

    # Menutup socket

    server_socket.close()

def receive_message():
    # Menentukan alamat IP dan port untuk server
    server_ip = '127.0.0.1'
    server_port = 8000

    # Membuat socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mengikat socket ke alamat IP dan port
    server_socket.bind((server_ip, server_port))

    # Mendengarkan koneksi masuk
    server_socket.listen()

    # Menerima koneksi dari pengguna lain
    client_socket, client_address = server_socket.accept()
    print(f"Terhubung dengan {client_address}")

    # Menerima pesan dari pengguna lain dan menampilkannya
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Pesan baru: {message}")

    # Menutup socket
    client_socket.close()
def main():
    # Membuat thread untuk mengirim pesan
    send_thread = threading.Thread(target=send_message)

    # Membuat thread untuk menerima pesan
    receive_thread = threading.Thread(target=receive_message)

    # Memulai thread
    send_thread.start()
    receive_thread.start()

    # Menunggu thread selesai
    send_thread.join()
    receive_thread.join()

if __name__ == '__main__':
    main()

import socket
import threading

def handle_client(client_socket, client_address):
    # Menerima pesan dari klien dan menampilkan di terminal server
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Pesan dari {client_address}: {message}")

def start_server():
    # Menentukan alamat IP dan port untuk server
    server_ip = '0.0.0.0'  # Menggunakan 0.0.0.0 agar dapat diakses dari perangkat lain dalam jaringan
    server_port = 8000

    # Membuat socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mengikat socket ke alamat IP dan port
    server_socket.bind((server_ip, server_port))

    # Mendengarkan koneksi masuk
    server_socket.listen(2)
    print("Server sudah berjalan. Menunggu koneksi...")

    while True:
        # Menerima koneksi dari klien
        client_socket, client_address = server_socket.accept()
        print(f"Terhubung dengan {client_address}")

        # Membuat thread untuk menangani koneksi klien
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def main():
    start_server()

if __name__ == '__main__':
    main()
import socket

def start_client():
    # Menentukan alamat IP dan port server
    server_ip = '0.0.0.0'  # Alamat IP server
    server_port = 8001

    # Membuat socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Menghubungkan socket ke server
    client_socket.connect((server_ip, server_port))

    # Mengirim pesan ke server
    while True:
        message = input("Pesan: ")
        client_socket.send(message.encode())

def main():
    start_client()

if __name__ == '__main__':
    main()

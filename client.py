import socket

client = socket.socket()

ip = '192.168.100.114'
port = 54500

client.connect((ip, port))


receive_message = client.recv(1024).decode('utf-8')
if receive_message:

    print(receive_message)
    while receive_message:
        print(receive_message)
        send_text = input('Enter your message: ').encode('utf-8')
        client.send(send_text)

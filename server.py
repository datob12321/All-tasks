import socket
import random
from pytube import YouTube


def download_music(music_url):
    try:
        url = music_url
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f'{video.title}.mp3')
        print(f"{video.title} has been downloaded!")
    except KeyError:
        print('No video was found! Please chck the url!')
    return f'{video.title}.mp3'


server = socket.socket()

ip = '192.168.100.114'
port = 54500

server.bind((ip, port))
server.listen()
conn, addr = server.accept()

if conn:
    print(f"Successful connection from {addr}")
    conn.send('Welcome to our server'.encode('utf-8'))

    receive_text = conn.recv(1024).decode('utf-8')
    while receive_text != 'stop':
        if receive_text.startswith('https://www.youtube.com/watch?'):

            try:
                down = download_music(receive_text)
                print('Received link: ', receive_text)
                print('name of the video:  ', down)
                conn.send(f'The music named : {down}'.encode('utf-8'))
                receive_text = conn.recv(1024).decode('utf-8')
            except:
                conn.send('Sorry, but the attempt of downloading music was not successful'
                        .encode('utf-8'))
        else:
            conn.send(receive_text.encode('utf-8'))
            print('Received text:', receive_text)
            break
else:
    print('exit')

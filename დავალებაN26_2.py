from pytube import YouTube
import concurrent.futures as features
import time

my_music_urs = ['https://www.youtube.com/watch?v=aSjflT_J0Xo',
                'https://www.youtube.com/watch?v=Mtau4v6foHA',
                'https://www.youtube.com/watch?v=6OQpVBnBU2I',
                'https://www.youtube.com/watch?v=EfF9EE6ZR5E',
                'https://www.youtube.com/watch?v=GmHrjFIWl6U',
                'https://www.youtube.com/watch?v=NUsoVlDFqZg',
                'https://www.youtube.com/watch?v=kJQP7kiw5Fk',
                'https://www.youtube.com/watch?v=wnJ6LuUFpMo',
                'https://www.youtube.com/watch?v=_I_D_8Z4sJE',
                'https://www.youtube.com/watch?v=U28pYrR8TI0']


def download_music(music_url):
    try:
        url = music_url
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f'{video.title}.mp3')
        print(f"{video.title} has been downloaded!")
    except KeyError:
        print('No video was found! Please chck the url!')


if __name__ == '__main__':

    start = time.time()

    with features.ProcessPoolExecutor() as p:
        p.map(download_music, my_music_urs)


    # k = list(map(download_music, my_music_urs))

    end = time.time()
    print(f'Time taken to download all musics - {end - start}')

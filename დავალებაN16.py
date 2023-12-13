import csv


class Music:
    objects = []
    artists = []
    genres = []
    musics = []

    def __init__(self, music_name: str, artist_name: str, genre: str, country: str):
        assert (len(music_name) > 2 and len(artist_name) > 2
                and len(genre) > 2 and len(country) > 2), 'It must have at least 3 symbol'

        assert (len(music_name) <= 20 and len(artist_name) <= 20
                and len(genre) <= 20 and len(country) <= 20), \
            "It mustn't have more than 20 symbol"

        self.__music_name = music_name
        self.artist_name = artist_name
        self.genre = genre
        self.county = country
        self.likes = 0
        if self.music_name not in Music.musics:
            Music.objects.append(self)
            Music.musics.append(self.__music_name)
        if self.artist_name not in Music.artists:
            Music.artists.append(self.artist_name)
        if self.genre not in Music.genres:
            Music.genres.append(self.genre)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__music_name})'

    @property
    def music_name(self):
        return self.__music_name

    @music_name.setter
    def music_name(self, value):
        if len(value) < 3:
            print("It must have at least 3 symbol")
        elif len(value) > 20:
            print("It mustn't have more than 20 symbol")
        elif value[0].lower() != self.__music_name[0].lower():
            print("The first letter of old and new name must be same")
        elif value[-1].lower() != self.__music_name[-1].lower():
            print("The last letter of old and new name must be same")
        else:
            self.__music_name = value

    @classmethod
    def show_music_index(cls, music: str):
        objs_list = [(v+1, i) for v, i in enumerate(cls.musics)]
        try:
            return objs_list[cls.musics.index(music)]
        except:
            return "Sorry, we have not music with such name!"

    @classmethod
    def musicOfArtist(cls, artist):
        musicList = []
        for obj in cls.objects:
            if obj.artist_name == artist:
                musicList.append(obj.__music_name)
        return musicList

    @classmethod
    def like_music(cls, music):
        for object in cls.objects:
            if object.__music_name == music:
                object.likes += 1

    @staticmethod
    def message():
        print('Listen to music, it is great. You will see it!')

    @staticmethod
    def create_obj():
        with open('music.csv', 'r') as file:
            music_info = list(csv.DictReader(file))
            for music in music_info:
                Music(music['music'], str(music['artist']), music['genre'], music['country'])

    def __return_likes(self):
        return self.likes

    def show_likes(self):
        k = self.__return_likes()
        print(f'"{self.__music_name}" has {k} likes.')


Music.create_obj()

music_objects = {}

for i, obj in enumerate(Music.objects):
    variable_name = f'music{i+1}'
    music_objects[variable_name] = obj


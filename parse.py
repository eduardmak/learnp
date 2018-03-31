import os
from sys import getdefaultencoding
from eyed3 import mp3


def get_tags(folder):
    if os.path.exists(folder):
        files_paths = []
        for path, subdirs, files in os.walk(folder):
            files_paths.extend([os.path.join(path, name) for name in files if name[-4:] == ".mp3"])
            #todo убрать дубликаты
        print(files_paths)
        tags_list = []
        for file in files_paths:
            f = mp3.Mp3AudioFile(file)
            if f.tag:
                # если нет жанра
                if f.tag.genre:
                    genr = f.tag.genre.name
                else:
                    genr = None
                # todo сделать обработку бардака с кодировками
                tags_list.append({"filepath": file, "title": f.tag.title, "artist": f.tag.artist, "album": f.tag.album,
                          "year": str(f.tag.getBestDate()), "genre": genr,"bitrate": f.info.bit_rate_str, "length": f.info.time_secs, })
            else:
                tags_list.append({"filepath": file, "title": None, "artist": None, "album": None, "year": None,"genre": None,
                          "bitrate": None, "length": None, })

        return tags_list

    else:
        return "Не правильно указан каталог!"

#Передаваться будут изменяемые значения, если не меняется передается None. Приходит json вида tags_list[{},{}]
#будут ли передаваться с формы сразу сюда? Как быстро обработать словарь не сравнивая каждый иф.
#

def edit_tags(tags_list):
    for i in tags_list:
        if i.get('filepath') and i.get('artist'):
            print(i.get('filepath'))
            f = mp3.Mp3AudioFile(i.get('filepath'))
            if i.get("title"):
                f.tag.artist = i.get("title")
            if i.get("artist"):
                print(i.get("artist"))
                f.tag.artist = i.get("artist")
            if i.get("album"):
                f.tag.album = i.get("album")
            if i.get("genre"):
                f.tag.genre.name = i.get("genre")
            # todo тут запись года

            f.tag.save()



def get_atr_test():
    path = r'C:\Python\mp3\audio\Face.mp3'
    f = mp3.Mp3AudioFile(path)
    title = f.tag.title
    artist = f.tag.artist
    album = f.tag.album
    year = f.tag.getBestDate()
    genre = f.tag.genre
    bitrate = f.info.bit_rate_str
    length = f.info.time_secs
    print(year)


# получить все фаилы в папке
# обработать каждый фаил в цикле
# вернуть список словарей


if __name__ == '__main__':
    get_tags('C:\Python\mp3\music')

# Название
# Исполнитель
# Альбом
# Год
# Жанр



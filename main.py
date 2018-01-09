#!/usr/bin/env python3.6

import sys
import mp3_class.mp3list


import search.search_in_directory as sid

try:
    # предполагается что на данном этапе наше приложение получает один аргумент коммандной строки
    # протестировано: python3.6 main.py /Users/MacUser/Music
    # В результате выдает список всех mp3 файлов в заданной директории с версиями и тегами

    mp3s = mp3_class.mp3list.MP3List([], mp3_class.mp3list.PickleSerializer())

    sid.find_all_mp3_in_current_dir(sys.argv[1], mp3s)
    mp3s.make_index('TIT2')
    for mp3 in mp3s.mp3s:
        print(mp3.full_path)
        print('{}\n{}\ntitle : {}\nartist: {}\nalbum : {}\n'.format(mp3.full_path,
                                                                    mp3.name,
                                                                    mp3.meta_data['TIT2'],
                                                                    mp3.meta_data['TPE1'],
                                                                    mp3.meta_data['TALB']))
    

# если файл будет запускаться не с коммандной строки и/или без параметров
except IndexError:
    print('Path parameter is empty, please restart the application and set the Path to directory with music')

except FileNotFoundError:
    print("Path [{}] does not exist".format(sys.argv[1]))


#!/usr/bin/env python3.6

import sys
import argparse
import mp3_class.mp3list

import search.search_in_directory as sid
import download.url_download as ud

def getparser():
    parser = argparse.ArgumentParser(description='Description here')
    subparsers = parser.add_subparsers(dest='command', help='List of commands')
    # A Find command
    search_parser = subparsers.add_parser('S', help='Searches local mp3 files')
    search_parser.add_argument('dirname', action='store', help='Directory to search')
    # A Download command
    down_parser = subparsers.add_parser('D', help='Downloads mp3 files from net')
    down_parser.add_argument('url', action='store', help='URL to download')
    # A Index command
    index_parser = subparsers.add_parser('I', help='Indexes collection by Tag')
    index_parser.add_argument('tag', action='store', help='Tag to index')
    # A PlayList command
    taglist_parser = subparsers.add_parser('P', help='Generate play-list by Tag')
    taglist_parser.add_argument('tag', action='store', help='Tag to select')
    taglist_parser.add_argument('value', action='store', help='Tag value')
    return arser.parse_args()


try:
    # протестировано: python3.6 main.py /Users/MacUser/Music

    args = getparser()
    mp3s = mp3_class.mp3list.MP3List([], mp3_class.mp3list.PickleSerializer())

    if args.command == 'S':
        sid.find_all_mp3_in_current_dir(args.dirname, mp3s)
    elif args.command == 'D':
        tracks = ud.links_parse_re(args.url)
        print(tracks)
        ud.download_tracks(tracks)
        print('OK')
    elif args.command == 'I':
        mp3s.make_index(args.tag)
    elif args.command == 'P':
        playlist = mp3_class.mp3list.PlayList()
        playlist.add_list(mp3s.export(args.tag,args.value))
        playlist.save('playlist.m3u')
    else:
        print('command line not recognize')

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


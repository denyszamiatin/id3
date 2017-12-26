#!/usr/bin/env python3.6

import os
import fnmatch
import mp3_class.mp3mutagen as id3


def find_all_mp3_in_current_dir(path, mp3s):

    if not os.path.isdir(path):
        raise FileNotFoundError

    for root, dirs, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, '*.mp3'):
                mp3s.add(id3.ID3Tags(os.path.join(root, file)))

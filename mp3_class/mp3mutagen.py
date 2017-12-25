import os
from mutagen.id3 import ID3

# ID3 tags description
# ['TCON'] Content type
# ['TIT2'] Title/songname/content description
# ['TPE1'] Lead performer(s)/Soloist(s)
# ['TRCK'] Track number/Position in set
# ['TALB'] Album/Movie/Show title
# ['TDRC'] Date


class ID3Tags:
    """ Class-description of mp3 file
        - file name
        - file path
        - ID3-tags
    """

    def __init__(self, path):
        self.full_path = path
        _, self.name = os.path.split(path)
        self.meta_data = self._parse_id3_tags()
        self.current_folder_name = self.full_path.rsplit(os.sep)[-2]

    def _parse_id3_tags(self):
        tags = ID3(self.full_path)
        return tags


class ID3List:
    """
    list of dictionaries with ID3 tags
    """

    def __init__(self, mp3s):
        self.mp3s = list(mp3s)
        # self.serializer = serializer

    def add(self, mp3):
        self.mp3s.append(mp3)

    # def serialize(self):
    #     self.serializer.serialize(self.mp3s)
    #
    # def deserialize(self):
    #     self.mp3s = self.serializer.deserialize()

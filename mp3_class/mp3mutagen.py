from mutagen.id3 import ID3
from . import mp3

# ID3 tags description
# ['TCON'] Content type
# ['TIT2'] Title/songname/content description
# ['TPE1'] Lead performer(s)/Soloist(s)
# ['TRCK'] Track number/Position in set
# ['TALB'] Album/Movie/Show title
# ['TDRC'] Date


class ID3Tags(mp3.MP3Format):
    """ Class-description of mp3 file
        - file name
        - file path
        - ID3-tags
    """

    def _parse_id3_tags(self):
        id3 = ID3(self.full_path)
        tags = {
            tag:id3.get(tag).text[0]
            for tag in id3
            if hasattr(id3.get(tag), 'text')
        }
        return tags

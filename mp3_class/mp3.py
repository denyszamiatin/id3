#!/usr/bin/env python3.6

import os
import struct


ID3_VERSION_LENGTH = 3


class ID3Decoder:
    ID3v = 'ID3'

    def __init__(self, fd):
        self.fd = fd

    def _get_minor_and_revisions(self):
        """
        Reads 2 bytes: the minor and revision versions.
        """

        __m_and_r_versions = struct.unpack("h", self.fd.read(2))

        version = '{}v{}.0'.format(
            self.ID3v,
            __m_and_r_versions[0]
        )

        if len(__m_and_r_versions) > 1:
            version += '.{}'.format(
                __m_and_r_versions[1]
            )

        return version

    def _get_flags(self):
        # 1 byte (first 4 bits): flags
        # здесь возможно пригодится bytearray
        flags = '{0:08b}'.format(ord(self.fd.read(1)))
        """
        http://id3.org/id3v2.4.0-structure
        flags
        a - Unsynchronisation
        b - Extended header
        c - Experimental indicator
        d - Footer present
        """
        return flags

    def _get_extended_header(self):
        # 4 bytes: The size of the extended header (if any), frames, and padding
        # afer unsynchronization. This is a sync safe integer, so only the
        # bottom 7 bits of each byte are used.
        extended_header = self.fd.read(4)
        return extended_header

    def decode(self):
        return {
            'version': self._get_minor_and_revisions(),
            'flags': self._get_flags(),
            'extended_header': self._get_extended_header(),
        }


decoders = {
    'ID3': ID3Decoder,  # Check if our file version is ID3v2
}


class MP3Format:
    """ Class-description of mp3 file
        - file name
        - file path
        - ID3-tags
    """

    def __init__(self, path):
        self.full_path = path
        _, self.name = os.path.split(path)
        self.meta_data = self._parse_id3_tags()
        self.current_folder_name = self.full_path.rsplit(os.sep)[-2]  # моя личная просьба оставить этот атрибут

    def _parse_id3_tags(self):
        with open(self.full_path, 'rb') as fd:
            ID3v = fd.read(ID3_VERSION_LENGTH).decode()
            decoder = decoders[ID3v](fd)
            return decoder.decode()

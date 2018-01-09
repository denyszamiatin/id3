import collections


class MP3List:
    """ mp3s - list of MP3Format objects
    serializer - serialise method (pickle, json etc)
    """

    def __init__(self, mp3s, serializer):
        self.mp3s = list(mp3s)
        self.indexes = {}
        self.serializer = serializer

    def make_index(self, tagname):
        self.indexes[tagname] = self._make_index(tagname)

    def _make_index(self, tagname):
        d = collections.defaultdict(list)
        for mp3 in self.mp3s:
            d[str(mp3.meta_data[tagname])].append(mp3)
        return d

    def add(self, mp3):
        self.mp3s.append(mp3)

    def serialize(self):
        self.serializer.serialize(self.mp3s)

    def deserialize(self):
        self.mp3s = self.serializer.deserialize()


class PickleSerializer:
    def __init__(self, filename='mp3list.lst'):
        self.filename = filename

    def serialize(self, obj):
        import pickle
        with open(self.filename, 'wb') as f:
            pickle.dump(obj, f)

    def deserialize(self):
        import pickle
        with open(self.filename, 'rb') as f:
            return pickle.load(f)

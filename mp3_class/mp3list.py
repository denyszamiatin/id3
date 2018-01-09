class MP3List:
    """ mp3s - list of MP3Format objects
    serializer - serialise method (pickle, json etc)
    """

    def __init__(self, mp3s, serializer):
        self.mp3s = list(mp3s)
        self.serializer = serializer

    def make_index_all(self):
        #self.index_TIT2 = self.indexing('TIT2')
        self.index_TPE1 = self.make_index('TPE1')
        self.index_TALB = self.make_index('TALB')

    def make_index(self, tagname):
        d = {}
        for mp3 in self.mp3s:
            tgnm = str(mp3.meta_data[tagname])
            if tgnm in d.keys():
                sps = d.get(tgnm)
            else:
                sps = []
            sps.append(mp3)
            d[tgnm] = sps
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

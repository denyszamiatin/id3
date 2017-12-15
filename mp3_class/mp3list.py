class MP3List:
    """ mp3s - list of MP3Format objects
    serializer - serialise method (pickle, json etc)
    """

    def __init__(self, mp3s, serializer):
        self.mp3s = list(mp3s)
        self.serializer = serializer

    def add(self, mp3):
        self.mp3s.append(mp3)

    def serialise(self):
        self.serializer.serialize(self.mp3s)


class PickleSerializer:
    def __init__(self, filename='mp3list.lst'):
        self.filename = filename

    def serialize(self, obj):
        import pickle
        with open(self.filename, 'wb') as f:
            pickle.dump(obj, f)

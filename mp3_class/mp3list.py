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
    def serialize(self, obj, filename='mp3list.lst'):
        import pickle
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)


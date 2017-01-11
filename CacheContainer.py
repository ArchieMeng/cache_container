import pickle
import os


class CacheContainer:
    def __init__(self, iterator=None):
        self.cache = []
        if iterator:
            for obj in iterator:
                self.dump(obj)

    def has_next(self):
        return len(self.cache) != 0

    def dump(self, obj, name="cache"):
        '''
        :obj type: object
        :return type:None
        '''
        cache_name = '{}{}.tmp'.format(name, len(self.cache))
        with open(cache_name, 'wb') as f:
            pickle.dump(obj, f, protocol=2)
        self.cache.append(cache_name)
        del obj

    def __iter__(self):
        return self

    def next(self):
        return self.load()

    def load(self):
        '''
        :return type: object:
        '''
        if self.has_next():
            cache_name = self.cache.pop(-1)
            with open(cache_name,'rb') as f:
                obj = pickle.load(f)
            os.remove(cache_name)
            return obj
        else:
            raise StopIteration

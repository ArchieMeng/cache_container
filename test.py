from CacheContainer import CacheContainer

cc = CacheContainer(range(5))

if cc.has_next():
    print True
else:
    print False

for obj in cc:
    print obj

if cc.has_next():
    print True
else:
    print False

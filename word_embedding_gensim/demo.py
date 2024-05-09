import gensim.downloader as api

wv = api.load("glove-wiki-gigaword-50")

print(wv["tower"])

pairs = [
    ("car", "minivan"),  # a minivan is a kind of car
    ("car", "bicycle"),  # still a wheeled vehicle
    ("car", "airplane"),  # ok, no wheels, but still a vehicle
    ("car", "cereal"),  # ... and so on
    ("car", "communism"),
]
for w1, w2 in pairs:
    print("%r\t%r\t%.2f" % (w1, w2, wv.similarity(w1, w2)))

print(wv.most_similar(positive=["car", "minivan"], topn=5))

print(wv.doesnt_match(["fire", "water", "land", "sea", "air", "car"]))

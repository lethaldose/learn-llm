import gensim.downloader as api
from numpy import dot

# matrix dot product 3x3 size
# explain steps
# 1*1 + 2*4 + 3*7 = 1 + 8 + 21 = 30
# 1*2 + 2*5 + 3*8 = 2 + 10 + 24 = 36
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(dot(a, b))

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

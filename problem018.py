import pandas as pd

def crawlup(chalice):
    for i in reversed(range(len(chalice) - 1)):
        for j in range(len(chalice[i])):
            chalice[i][j] += max(chalice[i + 1][j], chalice[i + 1][j + 1])
    return chalice[0][0]

t = []

triangle = pd.read_csv('15-layertriangle.csv', header = None)
layers = triangle.size
for i in range(layers):
    t.append(list(map(lambda x: int(x), triangle.iloc[i, 0].split(' '))))
print(crawlup(t))

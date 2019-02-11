from collections import Counter, defaultdict

file =open('file') 
file = file.read().split()

result = defaultdict(lambda: [0, []])
for i, l in enumerate(file): 
    for k, v in Counter(l.split()).items():
        result[k][0] += v
        result[k][1].append(i+1)

items = sorted(result.items(), key=lambda t: (-t[1][0], t[0].lower()))
for k, v in items:
    print('{1} {0} {2}'.format(k, *v))

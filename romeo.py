def read_url(url):
    import urllib.request
    try:
        with urllib.request.urlopen(url) as webpage:
            text = webpage.read().decode('utf-8')
        return text
    except Exception as e: 
        return e

s=read_url("http://dfedorov.spb.ru/python3/src/romeo.txt").split()

d = dict()
for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

print(d)

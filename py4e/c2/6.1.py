# Finding the top 10 most common words on a file -
fname = input('Enter romeo.txt -')
fhandle = open(fname)
histo = dict()
for lines in fhandle:
    words = lines.split()
    for word in words:
        histo[word] = histo.get(word, 0) + 1
# print(sorted (  [  (v, k) for k, v in histo.items()  ], reverse = True )  )
# - expert method - list comprehension creates a
# dynamic list. In this case we make a list of reversed tuples and then sort it.
slist = list()
for k, v in histo.items():
    # Creating a list of tupples -
    slist.append( (v, k) )

slist.sort(Reverse = True)

for val, key in slist:
    print(key, val)

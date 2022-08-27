# Dictionaries
# A list is a liner collection of elements which stays in order.
# A Dictionary is a bag of values, each with it's own lable.

print('Dictionaries basics')
purse = dict()
purse['money'] = 120
purse['tissue'] = 30
purse['candy'] = 5
print(purse)
print(purse['candy'])
purse['candy'] += 3
print(purse['candy'])

# Lists have indexes and Dictionaries have labels for calling purpose.

print("\nLists and Dictionaries\n")
print('Lists-')
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst, '\n')

print('Dictionaries-')
ddd = dict()
ddd['age'] = 21
ddd['courses'] = 183
print(ddd)
ddd['age'] = 23
print(ddd)

# Declaring a constant Dictionary
siblings = {'raj' : 19,18 , 'smeet' : 26, 'megha' : 21}
print('line 36 ', siblings)

# Counting the number of times a word appeared in a list.
pocket = dict()
names = ['raj', 'smeet', 'megha', 'shreya', 'akshara', 'raj', 'megha'] # list of strings.
for name in names:
    if name not in pocket:
        pocket[name] = 1
    else:
        pocket[name] += 1
print(pocket)

# get function, only for Dictionaries.

x =  pocket.get('raj', 0) #initialize

# Another way of doing that last example-
count = dict()
names = ['bob', 'marley', 'harry', 'harry']
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)

# Counting the number of times a word has appeared in a file and stoing it in dictionary -
fhandle = open('romeo.txt')
cfile = fhandle.read()
words = cfile.split() # Creating a list of words.
counter = dict()

for word in words:
    counter[word] = counter.get(word, 0) + 1
print('count -', counter)

print('\n')
# Counting the number of times, a word has appeared in a line-
counter = dict()
line = input('Please enter a line - ')
words = line.split()
print('words -', words)
for word in words:
    counter[word] = counter.get(word, 0) + 1
print('count -', counter)

# Getting 'List' of keys or values or both from 'Dictionary'
# using dictionary from line 35
print(list(siblings))
keylist = siblings.keys()
print(keylist)
print(siblings.values())
print(siblings.items())

# We loops through the key value pair of a dictionary using *two* iteration variables and in
# those iterations the first value is the key and the second is the corresponding value of that key.
print('\niterating through a dictionary')
for k,v in siblings.items():
    print(k, v)

# Counting the number of times, a word has appeared in a file and then printing the most occuring word-
fname = input('please enter a file name (either Me or romeo) :')
handle = open(fname)
histogram = dict()
for lines in handle:
    words = lines.split()
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

bigword = None
bigcount = None
for word,count in histogram.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print('Most occuring word in the file is - ', bigword)
print('And it occured ', bigcount, 'times')

input()

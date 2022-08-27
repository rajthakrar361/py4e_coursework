print('Printing letters of a word with their index')
fruit = 'banana'
index = 0
while index < len(fruit):
    print(index, fruit[index])
    index += 1

# other way of doing This
print('\nPrinting letters of a word')
for letter in fruit:
    print(letter)

# counting the number of times a letter appeared in a string
print('\ncounting the number of times a specefic letter appeared in a string')
word = input('Please enter a word: ')
alpha = input('Please enter the alphabet: ')
count = 0
for letter in word:
    if letter == alpha:
        count += 1
print(count)

#slicing strings
print('\nSlicing the string "Raj Thakrar"')
s = 'Raj Thakrar'
print(s[0:3])
print(s[0:])
print(s[4:])

# The 'in' keyword can also be used to check if one string is in the other string. It outputs either true or false.
print('\nUsing in to find a string in other string')
fruit = 'Dragon Fruit'
if 'Dragon' in fruit:
    print("Yes")

# Comparing Strings
print('\nComparing Strings')
word = 'Ram'
if word == 'Raj':
    print('Same')
if word < 'raj':
    print('Ram is smallerr them raj coz r is bigger than 'R'')

# USing lower() function. Syntaxt - string.lower(). it just gives out a copy in lowercase. Similarly we have upper too.
print('\nUSing upper and lower function')
print('RAj Thakrar'.lower())
s = 'RAM rajya'
print(s.upper())
# There are many more such functions from string library having same syntaxt.

# in says if na is in banana and find says where is na in banana
print('\nUsing find function')
fruit = 'ppaale'
stringg = fruit.find('pa')
print(stringg)

# Replace function
print('\nUSing replace function')
name = 'raaj'
news = name.replace('a', 'o')
print(news)

# string.lstrip() and string.rstrip() removes white spaces from left and right. and strip sab nikaldega, r and l.
# string.startwith('please') gives true and false if it starts with please.

# Practise
data = 'my email- id is raj.thakrar030601@gmail.com '
start = data.find('@')
stop = data.find(' ', start) # find is finding space. start is the index number where find with start looking from.
host = data[start + 1 : stop] # String slicing.

print(host)

input()

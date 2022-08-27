# Regular expression -

print('Usual method using find -')

fname = input('File name: ')
fhandle = open(fname)
for lines in fhandle:
    line = lines.rstrip()
    if line.find('From:') >= 0: # Every line containing From: will be printed.
        print(line)

print('Using Regular expression -')
import re

fname = input('File name: ')
fhandle = open(fname)
for lines in fhandle:
    line = lines.rstrip()
    if re.search('From:', line):
        print(line)

# Hence line 9 and line 19 does the same function
# Similarly following lines would do the same function -
# if line.startswith('From:'):
# if re.search('^From:', line):
# Now '^X.*:' would give us lines that 'startswith('X')' and then have any number of characters then end with ':' (* meant any number of character)
# For example - 'X-Boom: raj.thakrar030601@gmail.com' but will also include 'X-Boom Boom Boom: raj.thakrar' which we dont want
# This is solved by using - '^X-\S+:' where \S means match any non whitespace characters.

# Findall function
x = 'My age is 21 and i will be 22 soon. Actually in just 1 year i will be 32000.'
y = re.findall('[0-2]+', x)
print(y)
z = re.findall('[0-9a-z]+', x)
print(z)

# Greedy - '^F.+:' and non greedy - '^F.+?:'
import re
x = 'From: raj.thakrar@gmail.com Sat 03/06/2020'
y = re.findall('^From: (\S+@\S+)', x)
print(y)
z = re.findall('@(\S+)', x)
print(z)
input()

# A file handle open for read can be treated as a sequence of strings where lines in file constitue these strings.
# And we use for loop for iterating through a sequence.

# Counting the number of lines in a file
count = 0
fname = input('Enter Me.txt : ')
fhandle = open(fname)
for strings in fhandle:
    count += 1
    strings = strings.rstrip() #to avoid double newline (\n) character
    print(strings)
print('\nthe number of lines in the line is', count)

# Using file_handle.read() we can read the whole file as a single string.

# Read function - reads the whole file as a single string
# Counting the number of letters in a file.
print('\nCounting the number of words in a file.')
fhandle = open('Me.txt', 'r')
inp = fhandle.read()
print(len(inp))

# Searching for specefic lines through a file_handle
print('\nSearching for specefic lines (starting with email id) through a file_handle')
fhandle = open('Me.txt', 'r')
for lines in fhandle:
    if lines.startswith('email id'):
        lines = lines.rstrip()
        print(lines)

# Finding part of string in the file.
print('\nFinding strings with Thakrar word mentioned in them in the file.')
fhandle = open('Me.txt', 'r')
for lines in fhandle:
    if not 'Thakrar' in lines:
        continue
    lines = lines.rstrip()
    print(lines)

input()

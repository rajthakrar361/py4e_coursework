# Open the file romeo.txt and read it line by line. For each line,
#split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line
#check to see if the word is already in the list and if not append it to the list. When the program completes,
#sort and print the resulting words in alphabetical order.

fname = input("Enter file name:(romeo.txt) ")
fh = open(fname)
# Read function makes the file a single string
file = fh.read()
# Making a list of words.
words = file.split()
final = list()
# We also count the number of words in the file.
count = 0
for word in words:
    count = count + 1
    if word not in final:
        final.append(word)
final.sort()
print(count)
print(final)
input()

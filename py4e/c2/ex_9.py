# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
# of mail messages. The program looks for 'From ' lines and takes the second word of those lines as
# the person who sent the mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.


fname = input("Enter file name:(mbox-short.txt) ")
fh = open(fname)
histogram = dict()
for lines in fh:
    if lines.startswith('From:'):
        continue
    if lines.startswith('From'):
        words = lines.split()
        word = words[1]
        histogram[word] = histogram.get(word, 0) + 1

bigword = None
bigcount = None
for a,b in histogram.items():
    if bigcount is None or b > bigcount:
        bigword = a
        bigcount = b
print(bigword, bigcount)
input()

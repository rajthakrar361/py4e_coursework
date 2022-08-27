#Write a program to read through the mbox-short.txt and figure out the distribution by hour
#of the day for each of the messages. You can pull the hour out from the 'From ' line by finding
#the time and then splitting the string a second time using a colon.
#  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Please enter the file name (mbox-short.txt)')
fhandle = open(fname)
histo = dict()
for lines in fhandle:
    if lines.startswith('From:'):
        continue
    if lines.startswith('From'):
        words = lines.split()
        word = words[5]
        hours = word.split(':')
        hour = hours[0]
        histo[hour] = histo.get(hour, 0) + 1
alist = list()
for key, val in histo.items():
    # creating a list of tuple -
    alist.append( (key, val) )
alist.sort()
for h, t in alist:
    print(h, t)

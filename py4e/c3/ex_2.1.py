import re
fname = input('Enter File_name (ex.txt): ')
handle = open(fname)
numlist = list()
sum = 0
for line in handle:
    list = re.findall('[0-9]+', line)
    l = len(list)
    while l > 0:
        sum += int(list[l - 1])
        l -= 1
print(sum)

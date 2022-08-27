# Algorithms are set of rules used to solve problems
# Data structures is a particular way of organizing data in a computer

# Collection are variables which can have more than 1 value. For example a list is a collection.
# A list's element can be any python object, even another list.

print('Basics of a list')
list1 = [1, 2, [5, 6], 'red']
print(list1)
list2 = []
print(list2)
print(list1[3])
print(len(list1))

print('\nStrings are immutable - we cannot change the content of a string - we must make a new string to make any change.')
fruit = 'Banana'
# fruit[0] = 'b' -- this will result in a traceback
print(fruit.lower())

print('\nLists are mutable - We can change an element of a list using index operator')
list1[3] = 'blue'
print(list1)

print('\nusing range function')
friends = ['priyanshu', 'shreya', 'aditya',, 'Many more']
print(range(len(friends)))

# List can be sliced, concetanated, etc. Search list methods for more info.

# Adding things to list. append takes only 1 argument
print('\nAdding elements to list:')
list1.append('book')
list1.append(9)
print(list1)

if 9 in list1:
    print('\nwe can use "in" in lists too')
if 9 not in list1:
    print('we can use "not in" in lists too\n')

# Sorting function
list3 = [11, 2, 4, 3]
print('unsorted list -', list3)
list3.sort()
print('sorted list -', list3)
print("\n")

# Finding average of input values using appending values.
numlist = list()
while True:
    value = input('Please enter a number: ')
    if value == 'done':
        break
    value = float(value)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average is : ', average)

# Using Split function
aline = '\nfrom raj.thakrar030601@gmail.com saturday june 3 2020'
words = aline.split() # this will create a list of words.
print(words)
pieces = words[1].split('@')
host = pieces[1]
print('The host is ', host)


input()

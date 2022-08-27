# Tuples are unmodifiable lists using () instead of [].

# lists -
x = [1, 2, 3]
x[2] = 4
print(x)

# Tuples -
x = (1, 2, 3)
#x[2] = 4 - This line would creat a traceback.
# Hence tuples are immutable just like strings.
# You cant even sort, reverse or append tuple.

l = list()
dir(l)
t = tuple()
dir(t)
# For the above code terminal will show that tuple can only use count and index.

dict = {'raj' : 19, 'megha' : 21, 'smeet' : 28}
print('')
for (a,b) in dict.items(): #iterating through the dictionary.
    print(a,b)

# The items() method in dictionary returns a list of (key, value) tuples.
# Hence below, t is a list of tuples.

t = dict.items()
print(t)

# Sorted (in key order) Dictionary -
print('\nSorted Dictionary (key wise):')
for c, d in sorted(dict.items()):
    print(c, d)
print(t)

# Sorting dictionary in value order
print('\nSorted Dictionary (value wise):')
adict = {'a' : 5, 'b' : 100, 'c' : 15 }
print('The dict ->', adict)
alist = list()
for k, v in adict.items():
    # A list of tuple -
    alist.append( (v, k) )
print('the list ->', alist)
alist.sort(reverse = True)
# Same can be done using (a copy of alist is formed here) :- temp = sorted(alist, reverse = True)
print('The sorted list', alist)

input()

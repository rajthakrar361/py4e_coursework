import json

filename = 'mbox.txt'

dict1 = {}

with open(filename) as fh:

    for line in fh:
        command, description = line.strip().split(None, 1)
        dict1[command] = description.strip()

# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()

# JavaScript Object Notation (JSON)
# Data is in the form of dictionares or nested lists..has keys and values.
# line 8 is a key value pair
# phone is the key and its value is a dictionary

import json
data = '''{
    "name" : "Chuck",
    "phone" : {
    "type" : "intl",
    "number" : "+91 8780904975"
    },
    "email" : {
    "hide" : "yes"
    }
}'''

info = json.loads(data) # creating a dict named info
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])

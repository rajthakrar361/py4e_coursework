# Tags - indicates the start and the ending of elements.
# Tags contain attributes, text and other tags in it.
# Attributes - Keywords/value pairs on the opening tag of XML.
# Serialize - Convert data from one program into common format.
# De-serialize - conversion of data from a common format to a program.
# writing code in python to deal with XML.

import xml.etree.ElementTree as ET

data = '''<person>
    <name>Ra1j</name>
    <phone type="intl">
        +91 8780904975 #this number is a text
    </phone>
    <email hide = "yes"/> #hide is an attribute
    </person>'''

tree = ET.fromstring(data) #gives us a tree format of data.
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Next example- \n')
input = ''' <stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Raj</name>
        </user>
        <user x = "2">
            <id>009</id>
            <name>Mamba</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #makes list of user tags.
print('User count: ', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('Id: ', item.find('id').text)
    print('Attribute:', item.get("x"))

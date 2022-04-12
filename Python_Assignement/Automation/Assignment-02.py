import re

def regex_strip(s, chars = None):

    if chars == None:
        strip_left = re.compile(r'^\s*')
        strip_right = re.compile(r'\s*$')

        s = re.sub(strip_left, "", s)
        s = re.sub(strip_right, "", s)
    else:
        strip_left = re.compile(r'^[' + re.escape(chars) + r']*')
        strip_right = re.compile(r'[' + re.escape(chars) + r']*$')
        s = re.sub(strip_left, "", s)   
        s = re.sub(strip_right, "", s)
    return s
s = '.*    alphabetatheta   *4453   +-'
print(regex_strip(s, '.+-*'))

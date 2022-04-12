import re

madText = open('madText.txt', 'w')
text = 'An ADJECTIVE, a NOUN, a VERB and an ADVERB and a NOUN.'
madText.write(text)
madText.close()
content = re.split('(\W+)', text)

for i in content:
    if i == 'NOUN':
        content.insert(content.index('NOUN'), input('Replace ' + i + ': '))
        content.remove('NOUN')
    elif i == 'VERB':
        content.insert(content.index('VERB'), input('Replace ' + i + ': '))
        content.remove('VERB')
    elif i == 'ADVERB':
        content.insert(content.index('ADVERB'), input('Replace ' + i + ': '))
        content.remove('ADVERB')
    elif i == 'ADJECTIVE':
        content.insert(content.index('ADJECTIVE'), input('Replace ' + i + ': '))
        content.remove('ADJECTIVE')

content = ''.join(content)
print(content)
madLibs = open('madText2.txt', 'w')
madLibs.write(content)
madLibs.close()

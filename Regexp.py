import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

abc
'''

# Compile method will help us seperate out our patterns into a variable and also will make it easier to re-use the variable
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'abc')

# Finds all the occurence which follows the pattern
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])
print(text_to_search[266:269])
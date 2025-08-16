import re
""" pattern = "[\w._]+@[\w.]+"
txt = "My email address is alexandre.d.paquette@gmail.com and it is for personal use"
result = re.finditer(pattern, txt) #match will only search for the first word. Returns a match object
if result:
    print("Success!")
    print(result)
else:
    print("Failure") """

txt = "ATmega8, ATmega16, ATmega32"
x = re.findall("AT", txt)
print(x); print()

txt = "ATmega Microcontroller, mega"
x = re.search("mega", txt)
print(x); print()

txt = "A Momentary Laps of Reason"
x = re.split("\s", txt)
print(x); print()

txt = "A Momentary Laps of Reason"
x = re.sub("\s", "-", txt)
print(x); print()

text = "some sort of text with lots of ses"
pattern = re.compile(r'[sS]+')
matches = pattern.finditer(text)

counter = 0
for match in matches:
    counter += 1

print(counter)

text = "ATmega328 and ATmega8"
pattern = re.compile(r'mega')
matches = pattern.findall(r'mega')

for match in matches:
    print(match)
print

urls = """
https://www.google.com
http://canadorecollege.ca
https://www.nasa.gov
"""

genex = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
sub_urls = genex.sub(r'\2\3', urls)

print(sub_urls)
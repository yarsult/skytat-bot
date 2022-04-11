from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://rodon.org/other/trs.htm#a33"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = [chunk for chunk in chunks if chunk]

with open('dict1.txt', 'w') as f:
    for i in text:
        print(f'{i}', file=f)

with open('dict1.txt', 'r') as f:
    f1 = f.readlines()
print(f1)
with open('dict.txt', 'w') as f:
    for i in f1:
        if i != '\n':
            print(f'{i}', file=f)

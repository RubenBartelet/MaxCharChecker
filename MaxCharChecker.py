# Made by Ruben Bartelet on 4-2022
#version 1

from pathlib import Path

#the directory to the map
PROJECT_ROOT = Path(__file__).parent.parent

raw_text = PROJECT_ROOT / "the directory of the text file"

with open (raw_text, "r") as raw_text:
    raw_text_list = raw_text.read().splitlines()

ASCII_ = []
for a in range(0, 256):
    ASCII_.append(chr(a))

Letters = ['t','i','s','h']#which words can only be made with dots with morse code
Characters = ASCII_
for b in range(len(Letters)):
    Characters.remove(Letters[b])


List = []
for g in range(0, len(raw_text_list)):
    word = raw_text_list[g].lower()
    boolean = True
    for a in range(len(Characters)):
        if Characters[a] in word:
            boolean = False
    if boolean:
        List.append(word)

print(max(List, key=len))

  


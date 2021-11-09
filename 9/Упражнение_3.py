import os
from pathlib import Path
import re

class TextLoader:
    def __init__(self, adress):
        self.path = adress
        self.files_list = [x for x in list(os.listdir(self.path))]
        self.iterable = iter(self.files_list)

    def __len__(self):
        return len(self.files_list)

    def __getitem__(self, path):
        return new(path)

    def new(self, path):
        file = open(path, "r+t", encoding='utf-8')

        text = ''
        for line in file:
            line = line.lower()
            line = re.sub(r'[^\w\s]', '', line)
            text += '\n'
            text += line
        file.close()
        return text

    def __iter__(self):
        return self

    def __next__(self):
        file_path = next(self.iterable)
        print(file_path)
        text = self.new(file_path)
        return text


text = TextLoader('sample')
os.chdir('sample')

print(text.files_list) 
for i in text:
    print(i)

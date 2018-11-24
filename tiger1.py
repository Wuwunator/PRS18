# -*- coding: utf-8 -*-


f = open('tiger-word-tags.txt', encoding='utf-8')
tags_to_words = dict()

for l in f:
    fields = l.split()

    if len(fields) == 2:

        if fields[1] not in tags_to_words:
            tags_to_words[fields[1]] = set()
        tags_to_words[fields[1]].add(fields[0])


f.close()
from pprint import pprint as print
print(tags_to_words)

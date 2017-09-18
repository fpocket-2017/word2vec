# coding: utf-8

import csv
import MeCab
import re

tagger = MeCab.Tagger('-Owakati')
fo = open('tweets_owakati.txt', 'w')

for line in csv.reader(open('tweets.csv')):
    line = line[5]
    line = re.sub('https?://.*', '', line)
    fo.write(tagger.parse(line))

fo.close()

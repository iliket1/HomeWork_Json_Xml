import xml.etree.ElementTree as ET
import json
from collections import Counter

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

news_list = root.findall('channel/item/description')
words = []
for news in news_list:
  for word in news.text.lower().split():
      if len(word) > 6:
            words.append(word)
words_freq_count = Counter(words).most_common(10)
words_freq = []
for word_freq in words_freq_count:
    words_freq.append(word_freq[0])
print(words_freq)


with open("newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

news_list = json_data["rss"]["channel"]["items"]
description = [news['description'] for news in news_list]
words = []
for news in description:
  for word in news.lower().split():
      if len(word) > 6:
            words.append(word)
words_freq_count = Counter(words).most_common(10)
words_freq = []
for word_freq in words_freq_count:
    words_freq.append(word_freq[0])
print(words_freq)
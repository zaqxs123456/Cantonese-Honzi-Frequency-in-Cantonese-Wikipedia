import xml.etree.ElementTree as ET
import re
import json
import sys
import codecs

tree = ET.parse(sys.argv[1])

all_freq = {}
all_can_str = ET.tostring(tree.getroot(), encoding='unicode', method='text')

for i in all_can_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

sorted_can_str = {k: v for k, v in sorted(all_freq.items(), key=lambda item: item[1], reverse=True)}

honzi = {}

for key in sorted_can_str:
    if re.match(pattern=r'[\u4e00-\u9fff\u3400-\u4db5\U00020000-\U0002A6DF\U0002A700-\U0002B73F\U0002B740-\U0002B81F'
                        r'\U0002B820-\U0002CEAF\U0002CEB0-\U0002EBEF]+', string=key):
        honzi[key] = sorted_can_str[key]

with codecs.open(sys.argv[2], 'w', encoding='utf-8') as f:
    json.dump(honzi, f, ensure_ascii=False)
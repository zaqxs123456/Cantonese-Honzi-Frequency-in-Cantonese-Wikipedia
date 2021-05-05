import xml.etree.ElementTree as ET
import re
import json
import sys
import codecs

print(sys.argv[1])
tree = ET.parse(sys.argv[1])

all_freq = {}
all_can_str = ET.tostring(tree.getroot(), encoding='unicode', method='text')

for i in all_can_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

sorted_can_str = {k: v for k, v in sorted(all_freq.items(), key=lambda item: item[1], reverse=True)}

non_honzi = []

for key in sorted_can_str:
    if not re.match(pattern=r'[\u4e00-\u9fff]+', string=key):
        non_honzi.append(key)

for key in non_honzi:
    if key in sorted_can_str:
        del sorted_can_str[key]

with codecs.open(sys.argv[2], 'w', encoding='utf-8') as f:
    json.dump(sorted_can_str, f, ensure_ascii=False)
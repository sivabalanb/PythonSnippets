from collections import Counter
import string
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

for c in string.punctuation:
    paragraph = paragraph.replace(c, " ")

#count_w = paragraph.split(' ')
banned = ["bob", "hit"]

c = Counter(paragraph.lower().split())

for item, count in c.most_common():
    if item not in banned:
        # return item
        print(item)

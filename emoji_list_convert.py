import re

replace_emoji_list = []

with open('/Users/soshi/school/study/emoji_anlyze/emo_list.txt', encoding='utf-8') as file:
    for emoji_index in file:
        replace_emoji = re.sub(r'[0-9]+', '', emoji_index).replace('\n', '').strip()
        replace_emoji_list += replace_emoji
    print(replace_emoji_list)

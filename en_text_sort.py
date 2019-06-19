import re

replace_emoji_list = []
count = 1
with open('/Users/soshi/school/study/emoji_anlyze/emo_list.txt', encoding='utf-8') as file:
    for emoji_index in file:
        replace_emoji = re.sub(r'[0-9]+', '', emoji_index).replace('\n', '').strip()
        replace_emoji_list += replace_emoji

with open('/Users/soshi/school/study/emoji_anlyze/masyorizumi_en_emo.txt', encoding='UTF-8') as file:
    sentence_data = file.readlines()
    for emoji in replace_emoji_list[0]:
        for sentence_datum in sentence_data:
            if emoji in sentence_datum:
                with open('/Users/soshi/school/study/emoji_anlyze/test.csv',
                          mode='a', encoding='UTF-8') as write_file:
                    print(emoji)
                    write_file.write(sentence_datum.replace('\n', '') + "ぉ" + emoji + "\n")

        count += 1

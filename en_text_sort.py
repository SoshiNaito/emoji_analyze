import re

from insert_head import insert_head

replace_emoji_list = []
count = 0
with open('/Users/soshi/school/study/emoji_anlyze/emo_list.txt', encoding='utf-8') as file:
    for emoji_index in file:
        replace_emoji = re.sub(r'[0-9]+', '', emoji_index).replace('\n', '').strip()
        replace_emoji_list += replace_emoji

with open('/Users/soshi/school/study/emoji_anlyze/masyorizumi_en_emo.txt', encoding='UTF-8') as file:
    sentence_data = file.readlines()
    for emoji in replace_emoji_list:
        count += 1
        print(emoji)
        for sentence_datum in sentence_data:
            if emoji in sentence_datum:
                with open(
                        '/Users/soshi/school/study/emoji_anlyze/en_emoji_sentences/en_separate_' + str(count) + '.csv',
                        mode='a', encoding='UTF-8') as write_file:
                    write_file.write(sentence_datum.replace('\n', '') + "ぉ" + emoji + "\n")


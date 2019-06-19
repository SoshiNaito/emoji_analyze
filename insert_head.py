def insert_head():
    for i in range(1, 225):
        path_w = '/Users/soshi/school/study/emoji_anlyze/en_emoji_sentences/en_separate_' + str(i) + '.csv'

        with open(path_w) as f:
            l = f.readlines()

        l.insert(0, 'contentsぉemoji\n')

        with open(path_w, mode='w') as f:
            f.writelines(l)

        print(i)

import pandas as pd

for i in range(1, 225):
    data = pd.read_csv('/Users/soshi/school/study/emoji_anlyze/en_emoji_sentences/en_separate_' + str(i) + '.csv',
                       engine="python", sep='ぉ', quotechar='ぉ',
                       error_bad_lines=False)

    data.to_csv('/Users/soshi/school/study/emoji_anlyze/pd_shape_deta_dir/pd_shape_data_' + str(i) + '.csv')
    print(i)

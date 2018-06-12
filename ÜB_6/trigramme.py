# -*- coding: utf-8 -*-
# Wencke Hartwig
# 790786
# Uebungsblatt 6

# 1 N-Gramme

def find_trigrams(s):

    if len(s) < 3:
        print('This can not be divided in a trigram, sorry.')

    # leerzeichen und sonderzeichen beachten, leerzeichen und sonderzeichen vorher rauswerfen?
    # satzzeichen wie "?,!,."  string, symbol = s[0:-1], s[-1]

    cache = []

    for i in range(0, len(s) - 2):

        symbol = s[i]
        trigram = list(s[i:i+3])

        # list(s[0:3]) = ['a', 'b', 'r']
        # i wird immer eins größer, verschiebt sich immer eine stelle nach vorne



def count_or_add_trigrams(trigram, trigrams_so_far):

    for entry in trigrams_so_far:
        trigram = entry[0]
        if trigram == trigram:
            entry[1] += 1

            break

    else:
        trigrams_so_far.append([trigram, 1])
    return trigrams_so_far


example_list = ['zickezackezickezacke',
                'The quick brown fox jumps over the lazy dog.',
                'Can I go to sleep now?',
                'Schifffahrtskapitän',
                'a and b and c',
                '11']


#for trigram in example_list:
   # print(






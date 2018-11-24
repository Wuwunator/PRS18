# Head start.
# ask me for this solution: 6cb9ce6024b5fd41aebb86ccd40d8080

# this line is not needed, just for better output:
from pprint import pprint
# just remove the top line

def count_or_add_trigrams(trigram, trigrams_so_far):
    '''
    Takes a trigram, and a list of previously seen trigrams
    and yields the same list with all discovered and counted
    trigrams.
    Adds given trigram if not found,
    increments the trigram counter if found.
    '''

    for entry in trigrams_so_far:
        test_trigram = entry[0]
        if test_trigram == trigram:
            entry[1] += 1

            break

    else:
        trigrams_so_far.append([trigram, 1])
    return trigrams_so_far


test_trigrams = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['b', 'd', 'e'],
    ['d', 'e', 'f'],
    ['a', 'a', 'a'],
    ['d', 'e', 'f']
]

trigram_count = []
for trigram in test_trigrams:
    print('I have been given this trigram:', end=' ')
    pprint(trigram)
    trigram_count = count_or_add_trigrams(trigram, trigram_count)
    print('After finishing this operation, my data looks like:')
    pprint(trigram_count)
    print('-------------------------------------------------------------')

print('After doing all test trigrams, this is what I have:')
pprint(trigram_count)

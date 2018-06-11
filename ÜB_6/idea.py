# Head start.
# ask me for this solution: 6cb9ce6024b5fd41aebb86ccd40d8080

def count_or_add_trigrams(trigram, trigrams_so_far):
    '''
    Takes a trigram, and a list of previously seen trigrams
    and yields the same list with all discovered and counted
    trigrams.
    Adds given trigram if not found,
    increments the trigram counter if found.
    '''
    found = False
    for entry in trigrams_so_far:
        test_trigram = entry[0]
        if test_trigram == trigram:
            entry[1] += 1
            found = True
            break
    if not found:
        trigrams_so_far.append([trigram, 1])
    return trigrams_so_far

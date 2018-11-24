# -*- coding: utf-8 -*-
# Wencke Hartwig
# 790786
# Uebungsblatt 6

# 1 N-Gramme

# zuerst definieren wir uns eine funktion, welche die trigramme eines strings ermittelt
def find_trigrams(s):
# als ausnahme deklarieren wir, dass strings, die kleiner als 3 zeichen sind, nicht als trigramme behandelt werden
    if len(s) < 3:
        print('This can not be divided in a trigram, sorry.')
# wir erstellen eine leere liste, die im folgenden gefüllt wird
    cache = []
# nun erstellen wir eine schleife, die die trigramme eines strings aufführt
# dazu beginnen wir an der ersten stelle des string und enden an der stelle, an der keine trigramm bildung mehr
# möglich ist, also vor den letzten beiden stellen des string
    for i in range(0, len(s) - 2):
        symbol = s[i]
        # da i mit jedem durchgang der schleife um den wert 1 erhöht wird, nutzen wir dies um das "trigram-fenster"
        # immer einen index weiter zu schieben
        trigram = list(s[i:i+3])
        # die zuvor leere liste des cache füllt sich so durchgang für durchgang und kann am ende ausgegeben werden
        cache = count_or_add_trigrams(trigram, cache)

    return cache

# zum auflisten und zählen der trigramme definieren wir uns eine funktion, die eben dies macht: die trigramme des
# strings auflisten und bei mehrfach vorkommen die frequenz um 1 erhöht
def count_or_add_trigrams(trigram, trigrams_so_far):
    for entry in trigrams_so_far:
        # das zuerst herausgefundene trigram des string ist der erste eintrag in die liste
        test_trigram = entry[0]
        # falls das nächst gefundene trigram das selbe ist, wird die frequenz des schon vorhandenen, selben strings
        # erhöht, und wir springen aus der schleife heraus und beginnen den prozess wieder für das nächst kommende
        # trigram
        if test_trigram == trigram:
            entry[1] += 1

            break
    # wenn das trigram ein neues, noch nicht vorhandenes trigram in unserer liste ist, dann wird es neu hinzugefügt
    # mit einer frequenz von 1
    else:
        trigrams_so_far.append([trigram, 1])
    return trigrams_so_far

# die beispielstrings für die trigramme
example_list = ['zickezackezickezacke',
                'The quick brown fox jumps over the lazy dog.',
                'Can I go to sleep now?',
                'Schifffahrtskapitän',
                'a and b and c',
                '11']

# am ende lassen wir uns für jeden string der beispielstrings-liste die trigramme und ihre frequenz ausgeben
for example in example_list:
    result = find_trigrams(example)
    print(result)







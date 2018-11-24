# -*- coding: utf-8 -*-
# Wencke Hartwig
# 790786
# Uebungsblatt 9

# N-Gramme in TiGer


# zuerst definieren wir uns eine Funktion, welche aus einem textfile die tags herausnimmt und
# in eine Liste hinzufügt
def tag_counter(filename):
    f = open(filename, encoding='utf-8')
    # für das weitere Verfahren benötigen wir:
    # eine leere Liste für die aufzunehmenden tags
    tag_list = []
    # ein leeres dictionary für die tags samt anzahl
    counter = {}
    # und den Startwert der Aufzählung
    trigram_count = 0
    # wir geben an, dass für jede Zeile des textfile ein split ausgeführt werden soll,
    # damit wir im weiteren damit arbeiten können, dass das field[0] ein Wort, und das
    # field[1} der tag des Wortes ist
    for l in f.readlines():
        fields = l.split()
        # damit die leeren Zeilen des textfile, welche nach jedem fertigen Satz auftauchen, nicht
        # weiter Beachtung finden, geben wir die Länge von 2 an, mehr oder weniger fällt heraus
        if len(fields) == 2:
            # zu unserer tag-Liste fügen wir nun jedes 1te field hinzu, also die tags
            tag_list.append(fields[1])
            # dann legen wir fest, dass immer, wenn 3 tags auf diese Weise gefunden wurden,
            if len(tag_list) >= 3:
                # diese 3 tags in die tag-Liste aufgenomen werden, also ein Trigramm gebildet wurde
                trigram_count += 1
                trigram = tuple(tag_list)
                # nach diesem Vorgang löschen wir den Inhalt, um dann wieder von vorne zu beginnen,
                # bis alle tags aus dem textfile in Trigrammen gesammelt wurden
                del tag_list[0]
                # unser counter hat sich nun mit tags und deren frequency gefüllt
                # (Funktion count_trigram weiter unter)
                counter = count_trigram(trigram, counter)

        else:
            tag_list.clear()

    f.close()
    return (counter, trigram_count)

# die folgende Funktion nimmt sich die gebildeten Trigramme und ein dictionary, in welche die Trigramme (key)
# gelegt und deren Häufigkeit (value) aufgezählt wird
def count_trigram(trigram, dictionary):
    # wenn das gebildete Trigramm schon vorkommt, wird die Häufigkeit um eins erhöht
    if trigram in dictionary:
        dictionary[trigram] += 1
    # wenn das gebildete Trigramm noch nicht vorhanden ist, wird es hinzugefügt
    else:
        dictionary[trigram] = 1
    return dictionary

# die letzte Funktion ist für die spätere Ausgabe gedacht, sie definiert die Einträge des dictionary
def get_value(key_value_pair):
    return key_value_pair[1]


# für die Ausgabe in einer 5-spaltigen Tabelle gehen wir wie folgt vor
trigram_frequency, trigram_count = tag_counter('tiger-word-tags.txt')
# wir definieren uns eine Variable mit der Häufigkeit unserer Trigramme
items = trigram_frequency.items()
# diese können wir dann sortiert ausgeben, da eigentlich vom kleinsten in den größten Wert ausfeglistet wird,
# drehen wir dies durch reverse um, und fangen so mit dem am häufigsten vorkommenden Trigramm an
items = sorted(trigram_frequency.items(), key=get_value, reverse=True)
# letzlich lassen wir uns eine Tabelle ausgeben, in diesem Fall mit einer Linkseinrückung von 7 Stellen,
# da dies optisch passend ist
for key, value in items:
    print(f"{value:<7}{value / trigram_count:.7f} {key[0]:<7}{key[1]:<7}{key[2]:<7}")

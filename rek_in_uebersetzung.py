# -*- coding: utf-8 -*-
# Wencke Hartwig
# 790786
# Uebungsblatt 5

# 2 Numerische Funktion
# 2.2 (Rekursive) Interlineare Uebersetzung

#als erstes erstellen wir eine funktion, die einzelne eintraege eines woerterbuches nehmen und einen anderen eintrag zurueckgeben soll,
#die eintraege im woerterbuch sollen die deutschen und eglischen worte sein, der zurueckgegeben wert die uebersetzung, das englische wort also.
def translation(search_word, dictionary) :
	for entry in dictionary :
#wir nehmen die eintraege der liste und weisen dem jeweils ersten eintrag der liste die bedeutung "deutsches wort" und dem zweiten eintrag "englisches wort" zu
#hierzu nutzen wir den index der eintraege
		dt_word, en_word = entry[0], entry[1]
#wenn das wort das gesucht werden soll eines der deutschen woerter im woerterbuch entspricht, dann geben wir das dazu passende englische wort aus
		if search_word.lower() == dt_word.lower() :
			return en_word
#wenn das wort so nicht im woerterbuch vorkommt markieren wir es mit einem sternsymbol um darauf aufmerksam zu machen
	return search_word + '*'

#nun erstellen wir eine funktion, die einen ganzen "satz", wenn noetig wiederholt, in seine einzelnen bestandteile aufteilt und fuer jedes "wort" die
#uebersetzung nimmt
def translate(s, dictionary) :
#abbruchbedingung: wenn kein leerzeichen mehr vorhanden ist, ist der "satz" fertig und wird ausgegeben
	if not ' ' in s :
		return translation(s[0:-1], dictionary) + s[-1]
#rekursiver fall: solange wie leerzeichen vorhanden sind, wird durch split ein teil abgeschnitten und uebersetzt, solange bis alle teile uebersetzt sind
	else :
		de_word, rest = s.split(maxsplit=1)
		en_word = translation(de_word, dictionary)
		return en_word + ' ' + translate(rest, dictionary)
		

#woerterbuch
lex_list = [['Hund','dog'],['Katze','cat'],['Wetter','weather'],
['Sonne','sun'],['gut','good'],['schlecht','bad'],['Regen','rain'],
['mit','with'],['ist','is'],['besser','better'],['als','than'],
['der','the'],['die','the'],['das','the'],['Hitze','heat'],
['anstrengend','exhausting'],['in','in'],['Sommer','summertime'],
['diesem','this'],['blau','blue'],['nicht','not'],['rot','red'],
['Fahrrad','bicycle'],['und','and'],['Ich','I'],['mag','like'],
['mehr','more'],['den','the'],['nervig','annoying'],['Luft','air'],
['nach','after'],['riecht','smells'],['dem','the'],['bin','am'],
['müde','tired'],['aber','but'],['muss','must'],['arbeiten','work']
,['bis','until'],['Uhr','o clock'],['sieben','seven']]

#beispielsaetze, vorletzter und letzter satz lassen sich nicht uebersetzen
dt_satz = [
	'Die Luft nach dem Regen riecht gut.',
	'Ich bin müde aber ich muss arbeiten bis sieben Uhr.',
	'Die Hitze in diesem Sommer ist anstrengend.',
	'Das Fahrrad ist rot und nicht blau.',
	'Ich mag den Hund mehr als die Katze.',
	'Die Katze ist nervig.',
	'Er mag die Katze mehr als den Hund.',
	'Das Fahrrad ist eigentlich gelb.'
]

#zur veranschaulichung werden die saetze mit bezeichnung deutsch und engl
for de in dt_satz :
	en = translate(de, lex_list)
	print('deutsch:  ' + de)
	print('englisch: ' + en)
	print('') 



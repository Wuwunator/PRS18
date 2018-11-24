# -*- coding: utf-8 -*-
# Wencke Hartwig
# 790786
# Uebungsblatt 5

# 2 Numerische Funktion
# 2.1 (Iterative) Interlineare Uebersetzung

#als erstes erstellen wir eine funktion, die einzelne eintraege eines woerterbuches nehmen und einen anderen eintrag zurueckgeben soll,
#die eintraege im woerterbuch sollen die deutschen und eglischen worte sein, der zurueckgegeben wert die uebersetzung, das englische wort also.
def translation(search_word, dictionary) :
	for entry in dictionary :
#wir nehmen die eintraege der liste und weisen dem jeweils ersten eintrag der liste die bedeutung "deutsches wort" und dem zweiten eintrag "englisches wort" zu
#hierzu nutzen wir den index der eintraege
		dt_word, en_word = entry[0], entry[1]
#wenn das wort das gesucht werden soll eines der deutschen woerter im woerterbuch entspricht, dann geben wir das dazu passende englische wort aus
#damit groß und kleingeschriebene woerter gleich behandelt werden, schreiben wir alles im vergleich klein
		if search_word.lower() == dt_word.lower() :
			return en_word
#wenn das wort so nicht im woerterbuch vorkommt markieren wir es mit einem sternsymbol um darauf aufmerksam zu machen
	return search_word + '*'	

#nun erstellen wir eine funktion, die einen ganzen satz, hier zuerst als leerer cache deklariert, aufnimmt, dazu wieder die eintraege des woerterbuchs
#und uns am ende einen vollstaendigen satz wiedergibt (der satz bestehend aus den eintraegen des woerterbuchs)
def translate(s, dictionary) :
	cache = ''
#wir trennen die teile des satzes von interpunktionszeichen, da diese sonst als nicht vorhandener eintrag wiedergegeben werden
	sentence, symbol = s[0:-1], s[-1]
#nun teilen wir durch split den "satz" in "worte" auf, die dann einzeln durch die vorherige translation funktion uebersetzt werden
	for word in sentence.split() :
#nun besteht der cache aus dem jeweils uebersetzten "wort" einem leerzeichen und ggf. weiteren worten und am ende dem satzzeichen
		cache = cache + translation(word, dictionary) + ' ' 
#ausgabe des ganzen satzes mit großbuchstaben zum satzbeginn
	return (cache[0:-1] + symbol).capitalize()

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




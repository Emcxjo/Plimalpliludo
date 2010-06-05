#coding=UTF-8
#jen ludo kie la komputilo kalkulas nombron hazardan inter 0 kaj limo difinita de la uzanto kaj la ludanto devos trovi.


#Salutmesaĝo kaj difino de la limo
print 'Saluton homo!'
limo=input(' Ni ludos ludon kune. La komputilo produktos hazardan nombron inter 0 kaj la limo kiun vi difinos, ekz. 100. Ju pli alta la limo, des pli malfacila la ludo, kaj pli longa! Nun tajpu ajnan pozitivan nombron:')


#kalkulo de la hazarda nombro
import random
nombro=random.randint(0,limo)


# por TESTOFAZO nur ni printas la nombron
print nombro


#ludmesaĝo kaj difino de la provnombro
print "Bonege! Nun vi devos tajpi nombron kiun vi supozas esti la korekta. La komputilo diros al vi ĉu ĝi estas supera aŭ malsupera al la trovenda nombro. Poste vi povos reprovi entajpante alian nombron pli akuratan, ĝis kiam vi atingos sukceson!" 
provo=input('Nun entajpu provnombron:')

#while-funkcio, kerno de la ludo
while provo != nombro:
    if provo<=nombro:
	print 'Hej, faru pli!'
    else:
	print 'Hej, faru malpli!'
    provo=input('Reprovu:')
print 'Prave! La celnombro estas', provo, ',gratulon!'



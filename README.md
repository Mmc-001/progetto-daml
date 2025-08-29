# Progetto d'esame di Data Analysis in Experimental Physics with Machine Learning

Gruppo composto dagli studenti Luca Attinà, Sharis Feriotto e Matteo Marchisio Caprioglio

Il progetto consiste nello sviluppare un'architettura Convolutional Neural Network per l'identificazione di malattie delle piante, a partire dal dataset PlantVillage (https://www.tensorflow.org/datasets/catalog/plant_village).

Il dataset, contenente 38 classi suddivise per specie e per condizioni di salute della pianta, risulta sbilanciato in quanto il numero di elementi all'interno di ciascuna di esse varia significativamente.

In questo branch si è quindi intervenuti sul bilanciamento del training dataset attraverso quattro diverse strategie:
- la prima crea nelle classi sottorappresentate delle copie delle immagini in esse presenti fino al raggiungimento del numero di elementi nelle classi desiderato (i file ad essa riferiti sono contrassegnati dalla sigla 'sampl');
  
- la seconda crea nelle classi sottorappresentate delle copie delle immagini in esse presenti e le modifica attraverso delle trasformazioni che agiscono sui valori dei loro pixel (i file ad essa riferiti sono contrassegnati dalla sigla 'color');
  
- la terza crea nelle classi sottorappresentate delle copie delle immagini in esse presenti e le modifica attraverso delle trasformazioni di tipo spaziale (i file ad essa riferiti sono contrassegnati dalla sigla 'geo');
  
- la quarta crea nelle classi sottorappresentate delle copie delle immagini in esse presenti e le modifica combinando le due precendeti pipeline di data augmentation, dunque attraverso delle trasformazioni che agiscono sia sui valori dei pixel sia a livello spaziale (i file ad essa riferiti sono contrassegnati dalla sigla 'comb').

L'obiettivo di questo branch è quello di valutare quale sia la migliore strategia di bilanciamento tra quelle elencate; questa valutazione viene effettuata valutando la performance del modello base, e il numero di dati per classe nei vari dataset ('t') è stato fissato a 200 (in combinazione a tutte le strtategia è stato applicato anche downsampling sulle classi che superavano eccedevano nel numero di elementi rispetto a questo numero).

Una volta individuato il metodo migliore, si valuta la performance del modello base sul dataset ottenuto attraverso questa modalità di bilanciamento con il numero di elementi per classe t pari alla media matematica dei numeri di elementi per classe. 

Si è inoltre valutato come la scelta del numero ('t') di elementi all'interno delle classi incidesse sulla performance del modello comparando i risultati ottenuti con:
- 't' pari al numero di elementi nella classe più grande (i file ad essa riferiti sono segnalati dalla sigla '4399')
- 't' pari alla media matematica calcolata a partire da tutti i numeri di elemntenti (i file ad essa riferiti sono segnalati dalla sigla '1143')
- 't' pari al numero di elementi nella classe più piccola (i file ad essa riferiti sono segnalati dalla sigla '122').

# Progetto d'esame di Data Analysis in Experimental Physics with Machine Learning

Gruppo composto dagli studenti Luca Attinà, Sharis Feriotto e Matteo Marchisio Caprioglio

Il progetto consiste nello sviluppare un'architettura Convolutional Neural Network per l'identificazione di malattie delle piante, a partire dal dataset PlantVillage (https://www.tensorflow.org/datasets/catalog/plant_village).

Il dataset, contenente 38 classi suddivise per specie e per condizioni di salute della pianta, risulta sbilanciato, in quanto il numero di elementi all'interno di ciascuna di esse varia significativamente.

In questo branch si è quindi intervenuti sul bilanciamento del training dataset attraverso tre diverse strategie di data augmentation:
- la prima modifica le immagini originali attraverso delle trasformazioni di tipo spaziale (i file ad essa riferiti sono contrassegnati dalla sigla 'geo');
- la seconda modifica le immagini attraverso delle trasformazioni che agiscono sui valori dei loro pixel (i file ad essa riferiti sono contrassegnati dalla sigla 'color');
- la terza modifica le immagini applicanndo delle trasformazioni che agiscono sia sui valori dei pixel sia a livello spaziale (i file ad essa riferiti sono contrassegnati dalla sigla 'comb').

Si è inoltre valutato come la scelta del numero ('t') di elementi all'interno delle classi incidesse sulla performance del modello tra tre valori valutando i risultati per i seguenti tre scenari: 
- 't' pari al numero di elementi nella classe più grande (i file ad essa riferiti sono segnalati dalla sigla '4399')
- 't' pari alla media matematica calcolata a partire da tutti i numeri di elemntenti (i file ad essa riferiti sono segnalati dalla sigla '1143')
- 't' pari al numero di elementi nella classe più piccola (i file ad essa riferiti sono segnalati dalla sigla '122')

Quando necessario, per ridurre il numero di elementi all'interno delle classi è stato applicato down-sampling.

Una volta bilanciato il dataset, si è proceduto al training e all'evaluation del modello base (riportato nel branch comune 'main') per valutare l'effetto del bilanciamento sul dataset e confrontare i risultati ottenuti dalle diverse pipelines.

# Progetto d'esame di Data Analysis in Experimental Physics with Machine Learning

Gruppo composto dagli studenti Luca Attinà, Sharis Feriotto e Matteo Marchisio Caprioglio

Il progetto consiste nello sviluppare un'architettura Convolutional Neural Network per l'identificazione di malattie delle piante, a partire dal dataset PlantVillage (https://www.tensorflow.org/datasets/catalog/plant_village).

In questo branch mi sono occupato di esplorare l'impatto della capacità e della regolarizzazione del modello convoluzionale per ridurre l'overfitting dell'architettura base da cui siamo partiti tutti e tre: le training history e i plot di valutazione delle varie architetture sono salvati nelle cartelle appropriate.

Il training delle architetture avviene nel notebook model_training.ipynb, la valutazione di metriche quali overall accuracy, per-class ROC-AUC, precision, recall e f1-score nel notebook model_evaluation.ipynb.

I notebook possono essere eseguiti su Google Colab uploadando tutta la cartella su Google Drive, ma i modelli vanno ri-allenati per problemi di compatibilità sui file .h5 (file dei pesi) tra locale e Colab.
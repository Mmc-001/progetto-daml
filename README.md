# Progetto d'esame di Data Analysis in Experimental Physics with Machine Learning

Gruppo composto dagli studenti Luca Attinà, Sharis Feriotto e Matteo Marchisio Caprioglio

Il progetto consiste nello sviluppare un'architettura Convolutional Neural Network per l'identificazione di malattie delle piante, a partire dal dataset PlantVillage (https://www.tensorflow.org/datasets/catalog/plant_village).

Il mio obiettivo è stato quello di valutare le performance della rete base sul medesimo dataset ma con l'accorpamento delle immagini in 14 famiglie di piante, indipendentemente dalle malattie specifiche. Il compito è stato condotto partendo dal miglior modello base (a 2 layer convoluzionali) e operando fine tuning su Learning rate, coefficienti di regolarizzazione l2 e dropout rate. Inoltre ho provato ad utilizzare sia la classica Categorical Cross Entropy, sia la Focal Categorical Cross Entropy, essendo il dataset utilizzato sbilanciato. Infine, ho provato anche il metodo di transfer learning con architettura MobileNetV2.

Il training delle architetture CNN e CNN + transfer avviene rispettivamente nei notebook exam_proj_14_fams.ipynb e exam_proj_14_fams_transfer.ipynb. La valutazione di metriche quali overall accuracy, per-class ROC-AUC, precision, recall e f1-score nel notebook model_evaluation.ipynb (in caso di problemi con il caricamento dei modelli salvati in formato h5 è disponibile un modulo di valutazione alla fine di ogni notebook sopraccitato).

I notebook possono essere eseguiti su Google Colab uploadando tutta la cartella su Google Drive, ma i modelli vanno ri-allenati per problemi di compatibilità sui file .h5 (file dei pesi) tra locale e Colab.

A causa delle difficoltà riscontrate nell'importare il pacchetto in locale tramite comand tfds.load, i notebook sono forniti di un import in locale, implementabile ponendo la variabile COLAB = False e copiando in apposita directory la repository del dataset originale. Nel caso in cui il comando tfds.load funzioni senza problemi anche in locale, si può impostare COLAB = True ed eseguire tutto lo script. Se testato su COLAB, invece, indicare COLAB = True ed eseguire tutte le celle.
I file di training sono dotati di una funzione VERBOSE che permette di ottenere stampe per la valutazione qualitativa.

Nella cartella "weights" sono disponibili diverse versioni pre-addestrate in locale, ma a causa di alcuni problemi di compatibilità e/o importazione del dataset è possibile che i risultati siano discordanti con quelli ottenuti da run su Colab. Si consiglia pertanto di riaddestrare la rete e valutare il modello totalmente in locale o su colab, senza cambiare metodo di importazione del dataset.

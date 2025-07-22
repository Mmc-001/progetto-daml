# useful constants for each architecture
# to be used in the model_training.ipynb notebook
IMG_SIZE            = (128, 128) # Image size for resizing
BATCH_SIZE          = [64,
                       64,
                       64,
                       64,
                       64,]
N_EPOCHS            = [50,
                       50,
                       30,
                       30,
                       30,]
STARTING_LR         = [0.0002,
                       0.0002,
                       0.0002,
                       0.0002,
                       0.0002]
EARLY_PATIENCE      = [4,
                       4,
                       4,
                       4,
                       4]
REDUCE_LR_PATIENCE = [2,
                      3,
                      2,
                      2,
                      2]

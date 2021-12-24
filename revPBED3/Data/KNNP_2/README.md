# Kaolinite Neural Network: Generation 2 (KNNP_2)

This directory contains all data used to generate and train the second generation of the KNNP. 

## At a glance
- Datafile = 7000 Kaolinite frames.
- Symmetry Function = 511 symmetry functions.
- Stable? = Yes!
- Accurate? = Yes!
- Extrapolation? = Testing... 

## TrainingData

Contains all datafiles in `.xyz` format. For the sake of clarity and further analysis in the future, I've provided the both the *original* and *averaged* datafiles in this directory, as well as the mean value of the energy of the original dataframe.

All units provided within the datafiles are atomic units.  

## SymfuncData

Contains a number of different symmetry function files that were used to describe the training data (and any future data encountered by the NNP) to the neural network.

All units provided within the symmetry functions accommodate the atomic units used within  the training data. 

# Kaolinite Neural Network: Generation 1 (KNNP_1)

This directory contains all data used to generate and train the first generation of the KNNP. 

## At a glance

- Datafile = 6000 Kaolintie frames.
- Symmetry functions = 511 symmetry functions.
- Stable? = Mostly...
- Accurate? = Yes!
- Extrapolation? = Testing...

## TrainingData

Contains all datafiles in `.xyz` format. For the sake of clarity and further analysis in the future, I've provided the both the *original* and *averaged* datafiles in this directory, as well as the mean value of the energy of the original dataframe.

All units provided within the datafiles are atomic units.  

## SymfuncData

Contains a number of different symmetry function files that were used to describe the training data (and any future data encountered by the NNP) to the neural network.

All units provided within the symmetry functions accommodate the atomic units used within  the training data. 

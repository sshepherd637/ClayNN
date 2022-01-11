This directory contains all of the various models that have been created using data calculated using DFT at the revPBE + D3 level of theory. 

## Summary 

- KnnP_1:
    - Data = 6000 frames.
    - Symmetry functions = 511.

- KnnP_2:
    - Data = 7000 frames.
    - Symmetry functions = 511

## KnnP_1 

This is the first model that showed any real amount of accuracy and robustness when attempting simulation. This was created using 6000 frames of kaolinite taken from a DFTB simulation and recomputed at the revPBE + D3 level of theory to improve the accuracy of the energies and forces of the frames.

This model proved robust and accurate, as verified by both a committee model error analysis of the molecular dynamics outputs. Both NvT and NsT outputs showed a relatively accurate reproduction to revPBE + D3.

## KnnP_2

This model was created by adding data to `KnnP_1`. This data was obtained through the NsT simulations performed using `KnnP_1` where the simulation cell was observed to fluctuate between two 'longer lived' phases with different values for the cell parameter C. We have affectionately named these ***HighC*** and ***LowC*** accordingly. 500 frames of each system were randomly selected, recomputed and added to the training data of `KnnP_1`. 

As of writing, this model has been untested to see if this has improved upon any of the obtained properties of the NNP.

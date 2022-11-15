# Data

### MineralData

---

Contains all the structural information that was looked at when considering the construction of the potential. In addition, I've included a jupyter-notebook providing some details on how to convert from unit cell structure to supercell structure for these more complex minerals.

### SymFuncs

---

Contains files relating to the symmetry functions that are used in the creation and description of the atomic environments to the neural network. The total, **overcomplete** set is included along with a script that allows for the automatic creation of sets of symmetry functions. 

### revPBED3

---

Contains all the models used throughout this work created with the revPBED3 reference DFT functional. This directory includes the single 'driver' NNP and the committee used to validate it.

### revPBEvdW

---

Contains all the models used throughout this work created with the revPBEvdW reference DFT functional. This directory includes the single 'driver' NNP and the committee used to validate it.
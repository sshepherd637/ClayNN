# Clay Neural Network (ClaNN) Potentials

This repository is the location for all of the various models and data used in the creation of neural network potentials to describe the clay mineral, kaolinite. 

If you use any of the models located within this repository, please cite them accordingly!

# Directories
### Data

The Data directory contains all *general* data that is not specific to the individual potentials created using one of the listed DFT functionals. As such, the following information is located here...
1. SymFuncs: This directory contains all the information on the set of symmetry functions used to provide atomic descriptors within the potential.
2. MineralData: This directory contains all structural information used to provide various starting points for futher computation or comparisons throughout our work. 

---

### revPBE + D3

This directory contains all specific model information and files needed to recreate the use of this potential. The title refers to the DFT functional that the model is baselined against, namely revPBE with Grimme's dispersion corrections in the form of D3 corrections.

---

### revPBE + vdW

This directory contains all specific model information and files needed to recreate the use of this potential. The title refers to the DFT functional that the model is baselined against, namely revPBE with added dispersion corrections through the vdW corrections.

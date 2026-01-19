# Clay Neural Network (ClayNN) Potentials

This repository is the location for all of the various models and data used in the creation of neural network potentials to describe three of the dominant forms of the kaolin minerals, namely Kaolinite, Dickite, and Nacrite.

# Directories
### Data

The Data directory contains all *general* data that is not specific to the individual potentials created using one of the listed DFT functionals. As such, the following information is located here...
1. SymFuncs: This directory contains all the information on the set of symmetry functions used to provide atomic descriptors within the potential.
2. MineralData: This directory contains all structural information used to provide various starting points for futher computation or comparisons throughout our work. 
3. revPBED3: This directory contains all the required files to make up the ClayNN-D3 potential.
4. revPBEvdW: This directory contains all the required files to make up the ClayNN-vdW potential.
5. SCAN: This directory contains all the required files to make and run the ClayNN-SCAN potential. 
6. WannierCentre: This directory hosts the Wannier Centre models that were used to correct the predicted spectra obtained as the VDOS of Kaolinite in the later work. 


### InputFiles

The input file diirectory contains files that allow for the running of various calculations/simulations that we carried out throughout. We include files to run geometry optimization calculations and both classical and path integral molecular dynamics 'out of the box' while providing workflows for the creation of the phonon densities of states using phonopy. 

### External Codes

All DFT calculations performed when creating training data were completed with the use of AiiDA and the AiiDA-CP2K plugin. 

- [AiiDA] (https://www.aiida.net/index.html)
- [CP2K] (https://github.com/cp2k/cp2k.git)
- [AiiDA-CP2K] (https://github.com/aiidateam/aiida-cp2k)
- [I-PI] (https://github.com/i-pi/i-pi.git)
- [LAMMPS] (https://github.com/lammps/lammps.git)
- [Phonopy] (https://github.com/phonopy/phonopy.git)

### Citations 

Please cite the following publications in your work if you use any part of these models/datasets in your own workflows.

1. [A fully quantum-mechanical treatment for kaolinite](https://doi.org/10.1063/5.0152361)
2. [Transferability and expansion of the clayNN model](https://doi.org/10.1080/08927022.2025.2598392)
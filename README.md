# Clay Neural Network (ClayNN) Potentials

This repository is the location for all of the various models and data used in the creation of neural network potentials to describe the clay mineral, kaolinite. 

If you use any of the models located within this repository, please cite them accordingly!

# Directories
### Data

The Data directory contains all *general* data that is not specific to the individual potentials created using one of the listed DFT functionals. As such, the following information is located here...
1. SymFuncs: This directory contains all the information on the set of symmetry functions used to provide atomic descriptors within the potential.
2. MineralData: This directory contains all structural information used to provide various starting points for futher computation or comparisons throughout our work. 
3. revPBED3: This directory contains all the required files to make up the ClayNN-D3 potential.
4. revPBEvdW: This directory contains all the required files to make up the ClayNN-vdW potential.


### InputFiles

The input file diirectory contains files that allow for the running of various calculations/simulations that we carried out throughout. We include files to run geometry optimization calculations and both classical and path integral molecular dynamics 'out of the box' while providing workflows for the creation of the phonon densities of states using phonopy. 

### External Codes
- [CP2K] (https://github.com/cp2k/cp2k.git)
- [I-PI] (https://github.com/i-pi/i-pi.git)
- [LAMMPS] (https://github.com/lammps/lammps.git)
- [Phonopy] (https://github.com/phonopy/phonopy.git)
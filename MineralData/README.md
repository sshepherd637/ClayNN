This directory contains all the mineral data I have used or looked at throughout the creation of this NNP.

I'm not including every single frame as a single point of calculation, that would fill ***way*** to many needless directories, I'll instead put all the collected datafiles up here in their full glory whenever they are generated for each mineral investigated.

I'll provide a brief summary of each mineral here, to help clarify which one was used when and where. 

### Kaolinite

This mineral forms the majority of the data available to the NNP. I've included the `.cif` file and both the unit cell and supercell `.xyz` files. All data I have within the NNP which is some form of kaolinite is derived from the supercell file found here. 

### Dickite

Contains the `.cif` file, unit cell and supercell `.xyz` files. I used the supercell file to test the scope of the pure kaolinite NNP and then tested predictions of these frames later on. At this point there are no dickite frames within the potential.

### Nacrite

Contains the `.cif` file and unit cell `.xyz` file. I am yet to find a suitable supercell geometry that I am pleased with and is similar to that used for kaolinite.

### Halloysite

Contains both a 7A and 10A form of the original `.cif` and `.xyz` files. These frames are included here for completeness but may not ever be added to the potential based on the fact that kaolinite and halloysite only differ in their morphology at the nano scale, with halloysite being a tubular structure. The crystallographic data is extremely similar and as detailed in: 

D. Prishchenko, E. Zenkov , V. Mazurenko *et al.* *Molecular Dynamics of the Halloysite Nanotubes*, Phys. Chem. Chem. Phys. **2018**, pp.5841-5849, 20(8)

Halloysite can simply be treated as a larger scale version of kaolinite. 

As such, I'm not including any additional files on this mineral for the time being.

Finally, the file `SuperCell.ipynb` is a quick run-through of how a supercell can be made from an `.xyz` file using pythons `ase` module. In the version uploaded I am using the mineral nacrite.

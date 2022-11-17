# Molecular Dynamics Simulations

This directory contains all files required to run the molecular dynamics simulations used within this work. We provide universal input files in this directory and more specific files in the corresponding sub-directories. 

General files located in this directory and required to run all simulations include:
1. `md.lmp` : Lammps simulation input file.
2. `data.lmp` : Lammps data input file.
3. `ipi.xyz` : I-PI data input file. 

In this example, both `data.lmp` and `ipi.xyz` are the experimental kaolinite structure as a 2x2x2 supercell.

## Classical 

We provide input files for classical NVT, NST and NVE simulations, as `input.NVT.xml`, `input.NST.xml` and `input.NVE.xml` respectively.

## Quantum

As the general workflow was PIMD NVT -> PIMD NST -> PACMD/TRPMD NVT, we provide input files within corresponding sub-directories. These match the naming conventions described above. 
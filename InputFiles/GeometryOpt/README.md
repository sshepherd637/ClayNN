# Geometry Optimization

This directory contains all files required to run geometry optimization calculatons. We provide a general NNP Lammps input file that will require editing to use the NNP desired as `GeoOpt.NNP.lmp`. This uses the corresponding lammps data file in the form of `data.lmp`.

Both `GeoOpt.revPBEvdW.inp` and `GeoOpt.revPBED3.inp` are CP2K input files and therefore need a number of supplementary files to define the additional basis sets, psuedopotentials and dispersion parameters used within them. The necessary files are detailed here and provided within the Data directory of this repository. CP2K calculations use `kaolinite.xyz` as their data input file.

- `GeoOpt.revPBED3.inp`:
    - `POTENTIAL`
    - `GTH_BASIS_SETS`
    - `dftd3.dat`

- `GeoOpt.revPBEvdW.inp`:
    - `POTENTIAL`
    - `GTH_BASIS_SETS`
    - `vdW_kernel_table.dat`

Both `data.lmp` and `kaolinite.xyz` are of the experimental kaolinite structure in the 2x2x2 supercell form.
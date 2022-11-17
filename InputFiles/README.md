# Input Files

This directory is as mentioned in the title. We provide input files for geometry optimization, molecular dynamics simulations and workflows for PDOS computation and an exemplary Energy/Force computation for data creation. 

## Instructions for running
**Note: We do not recommend running geometry optimization calculations and path integral molecular dynamics on a local workstation, as they (especially the latter) will take substantial time to run.**

Following the installation of the necessary codes, these input files can be used as follows for parallel processes:

- Geometry Optimization

CP2K will depend on the available MPI libraries installed, we run it as:
    
    mpirun -np 96 /path/to/cp2k/bin/cp2k.popt -i GeoOpt.inp > GeoOpt.out 2>&1

LAMMPS is much more forgiving:
    
    mpirun -np 96 /path/to/lammps/bin/lmp_mpi < GeoOpt.lmp &> lmp.out

- Molecular Dynamics

Classical MD and PIMD calculations are run using the i-PI wrapper to LAMMPS. To run a simulation, use the following snippet:
    
    source /path/to/i-pi/bin/env.sh
    i-pi input_file.xml &> ipi.out &
    sleep 10
    mpirun -np 96 /path/to/lammps/bin/lmp_mpi < md.lmp &> lmp.out &
    wait
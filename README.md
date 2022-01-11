# KnnP
Repository to hold all different data for the creation of neural network potentials for kaolinite and it's polymorphs.

## MineralData

This directory contains all basic data used within the project. The following minerals are considered as suitable for this project.
 - Kaolinite: This is the main mineral being investigated as being archetypical of 1:1 type clays.
 - Dickite: A polymorph of kaolinite with an extremely similar composition.
 - Nacrite: Similar to Dickite.
 - Halloysite: This is a separate polymorph of kaolinite, however due to other research into the formation of halloysite nanotubes using kaolinite as the starting structure and working from there, I have not deemed it useful to include or investigate to any capacity. 

## revPBE0D3

This directory contains all data and models that used the hybrid functional revPBE0 with Grimme's D3 dispersion corrections. 

## revPBED3 

This directory contains all data and models that used the GGA functional revPBE with Grimme's D3 dispersion corrections.

## SymFuncs

This directory contains a quick script that is similar to the procedure I used to generate the entire symmetry function set before any further work was taken to scale the number of these to a more sensible number.

# Symmetry Functions

---

This directory contains all details of the **original** symmetry functions that were created in order to assign a unique description to all unique environments encountered in the kaolinite system. The initial set was created by hand prior to the creation of `QuickFuncs.py`. 

---

### Using `QuickFuncs.py`

If you plan on using `QuickFuncs.py` to create a symmetry set for whatever system you want to use them for, ***please use it with caution***.

The script in it's current iteration only creates G2, G3 and G9 symmetry functions for a given set of parameters. Any extension beyond this can follow a similar formalism as those provided within the script provided the necessary parameters are provided to the function. We refer the reader to [N2P2s symmetry function pages](https://compphysvienna.github.io/n2p2/api/symmetry_function_types.html) for more information on this topic.

The values provided to the script must be consistent with those you want to use both throughout the training procedure and those that you run molecular dynamics (there is _slightly_ more flexibility with the latter). The units used throughout the script as it sits are **atomic units**, i.e. Bohr.

This set of symmetry functions created by `QuickFuncs.py` was particularly useful at describing disordered solid surfaces. Different systems will likely require different functions beyond changing the elemental pairs/triplets found in the script, and some experimentation/optimization may be required.

In general, we recommend the _naive_ reader to create an overcomplete set of symmetry functions using something like the script provided. This may seem counter-intuitive when we want to create the most efficient model possible, but this ensures that we construct sufficient resolution into the atomic environments. N2P2 also offers ways to [reduce the number of symmetry functions](https://compphysvienna.github.io/n2p2/tools/nnp-prune.html) used in training if an overcomplete set is used throughout the workflow. 

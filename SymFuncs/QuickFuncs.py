#!/usr/bin/env python3

# Script to illustrate how the symmetry functions were created. This can be done interactively if desired using Jupyter-notebook.

# Import Modules
import os 

# Define basic lists of elements, ranges etc...
### ELEMENTS ###
elements = ['H', 'O', 'Al', 'Si']

### HARD CUTOFF VALUES ###
HardCutoffs = [8.0, 12.0]

### GAUSSIAN DISTRIBUTION WIDTHS ###
R8radialGaussWidths = [0.002, 0.015, 0.04, 0.075, 0.15, 0.3, 0.5, 0.75, 0.9, 1.75]
R8angularGaussWidths = [0.002, 0.04, 0.15, 0.75, 1.5]
R12radialGaussWidths = [0.001, 0.01, 0.03, 0.06, 0.1, 0.2, 0.4, 0.6, 0.8, 1.5]
R12angularGaussWidths = [0.001, 0.03, 0.1, 0.6, 1.0]

### GAUSSIAN CENTER SHIFTS ###
R8GaussShifts = [9.5, 8.0]
R12GaussShifts = [] 

### ANGULAR SYMFUNC PARAMETERS ###
PhaseShift = [1.0, -1.0]
ResolutionParam = [1.0, 2.0]

# Define a dictionary for ease of use and reference
OverlordDictionary = {
    'elements': elements,
    'radial cutoffs': HardCutoffs,
    'radial gaussian widths': [R8radialGaussWidths, R12radialGaussWidths],
    'radial gaussian shifts': [R8GaussShifts, R12GaussShifts],
    'angular gaussian widths': [R8angularGaussWidths, R12angularGaussWidths],
    'angular phase shift': PhaseShift,
    'angular resolution': ResolutionParam
}

def G2_writer(A_dict):
    G2_symfuncs = []
    for element_1 in A_dict['elements']:
        for element_2 in A_dict['elements']: # This ensures iteration over all pairs
            for cutoff in A_dict['radial cutoffs']: # This iterates over the different cutoffs
                for ii in range(len(A_dict['radial gaussian widths'][0])): # This accesses the individual widths corresponding the each cutoff
                    widthsets = A_dict['radial gaussian widths']
                    gaussShift = 0
                    if cutoff == 8.0:
                        gaussWidth = widthsets[0][ii]
                        if gaussWidth == 0.15:
                            gaussShift = A_dict['radial gaussian shifts'][0][0]
                        elif gaussWidth == 0.75:
                            gaussShift = A_dict['radial gaussian shifts'][0][1]
                    elif cutoff == 12.0:
                        gaussWidth = widthsets[1][ii]
                    G2_symfuncs.append(f'symfunction_short {element_1} 2 {element_2} {gaussWidth:.3} {float(gaussShift):.3} {float(cutoff):.3}\n')
            G2_symfuncs.append('\n')
    return G2_symfuncs
                        
def G3_writer(A_dict):
    G3_symfuncs = []
    for element_1 in A_dict['elements']:
        for element_2 in A_dict['elements']: # This ensures iteration over all pairs
            for element_3 in A_dict['elements']: # This iterates over all triplets
                for cutoff in A_dict['radial cutoffs']: # This iterates over the different cutoffs
                    for phase in A_dict['angular phase shift']: # This iterates over the phase shift
                        for resolution in A_dict['angular resolution']: # This iterates over the resolutiion parameter
                           for ii in range(len(A_dict['angular gaussian widths'][0])): # This accesses the individual widths corresponding the each cutoff
                                widthsets = A_dict['angular gaussian widths']
                                if cutoff == 8.0:
                                    gaussWidth = widthsets[0][ii]
                                elif cutoff == 12.0:
                                    gaussWidth = widthsets[1][ii]
                                G3_symfuncs.append(f'symfunction_short {element_1} 3 {element_2} {element_3} {gaussWidth:.3}  {phase:.2} {resolution:.2} {cutoff:.3}\n')
                G3_symfuncs.append('\n')
    return G3_symfuncs

def G9_writer(A_dict):
    G9_symfuncs = []
    for element_1 in A_dict['elements']:
        for element_2 in A_dict['elements']: # This ensures iteration over all pairs
            for element_3 in A_dict['elements']: # This iterates over all triplets
                for cutoff in A_dict['radial cutoffs']: # This iterates over the different cutoffs
                    for phase in A_dict['angular phase shift']: # This iterates over the phase shift
                        for resolution in A_dict['angular resolution']: # This iterates over the resolutiion parameter
                            for ii in range(len(A_dict['angular gaussian widths'][0])): # This accesses the individual widths corresponding the each cutoff
                                widthsets = A_dict['angular gaussian widths']
                                if cutoff == 8.0:
                                    gaussWidth = widthsets[0][ii]
                                elif cutoff == 12.0:
                                    gaussWidth = widthsets[1][ii]
                                G9_symfuncs.append(f'symfunction_short {element_1} 9 {element_2} {element_3} {gaussWidth:.3}  {phase:.2} {resolution:.2} {cutoff:.3}\n')
                G9_symfuncs.append('\n')
    return G9_symfuncs

def writer(A_dict):
    with open('symfuncs.txt', 'w+') as handle:
        handle.writelines("""### Symmetry Function File ###
        
## G2 type Symmetry Functions for radial distributions ###
""")
        G2funcs = G2_writer(A_dict)
        for func in G2funcs:
            handle.writelines(f'{func}')
        G3funcs = G3_writer(A_dict)
        handle.writelines('## G3 type Symmetry Functions for angular distributions ##\n')
        for func in G3funcs:
            handle.writelines(f'{func}')
        G9funcs = G9_writer(A_dict)
        handle.writelines('## G9 type Symmetry Functions for angular distributions ##\n')
        for func in G9funcs:
            handle.writelines(f'{func}')

if __name__ == "__main__":
    writer(OverlordDictionary)

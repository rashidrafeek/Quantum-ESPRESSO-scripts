# To create an xcrysden moviefile (.axsf) from a QE cp.x calculation.
# Run this in the folder containing .cel and .pos files.

# Set variables pertaining to the calculation and moviefile below.

# Needed packages: abipy

import abipy.iotools.xsf as xsf
from abipy.core.structure import Structure
import numpy as np

# Set variables here
pref = 'prefix'   # prefix of .cel and .pos files. ( [pref].pos )
sp = [1]*1 + [8]*2    # species atomic numbers in the order printed in .pos file eg., for H2O (in H-O-O order): [1]*1 + [8]*2 or explicitly as [1 8 8]
ns = 2000    # number of structures to be included in the movie (0 for taking all structures) 
skip_freq = 10   # number of structures to be skipped after each structure (0 for no skipping)

ang = 0.529177249

def divide_chunks(l, n):
     # looping till length l  
     for i in range(0, len(l), n):
          yield l[i:i + n]

# Reading Files
cellfile = open(pref+'.cel').read().splitlines()
posfile = open(pref+'.pos').read().splitlines()
lats = list(divide_chunks(cellfile, 4))
coords = list(divide_chunks(posfile, len(sp)+1))

# Loading Structures
structures = []
if(ns==0):
    ns = len(lats)
for i in range(0,ns,skip_freq):
     tlat = np.loadtxt(lats[i], skiprows=1).transpose()*ang
     tpos = np.loadtxt(coords[i], skiprows=1)*ang
     structures.append(Structure(tlat, sp, tpos, coords_are_cartesian=True))

# Writing output to '[pref]_movie.axsf'
f = open(pref+'_movie.axsf','w')
xsf.xsf_write_structure(f, structures)

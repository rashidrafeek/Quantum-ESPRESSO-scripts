# To create an ase trajectory (.traj) file from a QE cp.x calculation
# Run this in the folder containing .cel and .pos files.

# Set variables pertaining to the calculation below.

# Needed packages: ase

from ase import Atoms
import ase.io.trajectory as trj
import numpy as np

# Set variables here
pref = 'pref'   # prefix of .cel and .pos files. ( [pref].pos )
sp = [1]*1 +[8]*2    # species atomic numbers in the order printed in .pos file eg., for H2O (in H-O-O order): [1]*1 + [8]*2 or explicitly as [1 8 8]

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

# Loading Structures and writing trajectory file
asestrs = []
writer = trj.TrajectoryWriter(pref+'_ase'+'.traj')
for i in range(0,len(lats)):
     tlat = np.loadtxt(lats[i], skiprows=1).transpose()*ang
     tpos = np.loadtxt(coords[i], skiprows=1)*ang
     writer.write(atoms=Atoms(cell=tlat, numbers=sp, positions=tpos, pbc=True))
writer.close()

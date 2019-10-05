# Quantum-Espresso-scripts

Python scripts to postprocess Quantum Espresso calclations. Usage is described inside each script.

Included scripts:

1. cptoaxsf.py : create an xcrysden movie (.axsf) from a Quantum
     espresso CPMD calcultion.
    * Run the script in the folder containing .cel and .pos files after updating the variables in the script.
    * The output.axsf file can be visualized in xcrysden by running `xcrysden --axsf output.axsf`
  2. cptotraj.py: create an ASE trajectory (.traj) file from a QE cp.x calculation.
 * Run the script in the folder containing .cel and .pos files after updating the variables in the script.
  *   To visualize using ASE GUI: Run `ase gui [filename].traj` from command line.
 To import the trajectory file for further analysis in python, run:
      >     import ase.io.trajectory as trj
      >     reader = trj.TrajectoryReader('/path/filename.traj')

Most scripts require some of the following packages (mentioned in each script).

 - [abipy](https://abinit.github.io/abipy/installation.html)

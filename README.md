# SparseGaussianMolecule
MOLECULAR SPARSE REPRESENTATION BY 3D ELLIPSOID RADIAL BASIS FUNCTION NEURAL NETWORKS

The Gaussian surface is defined as 
```
{x: \sum_{i}exp(-d(||x-xi||^2 - ri^2)=c}
```
Instructions for MOLECULAR SPARSE REPRESENTATION (under Linux): 
1) Unpack SparseGaussianMolecule.tar.gz
   The SparseGaussianMolecule contains these folders:
   \pqr: directory for input .pqr files.
   \output: directory for output .txt files.
   \example: directory for a script main.py.
   (In main.py: The variable PQR is the file name of input .pqr file. It should be in the \pqr folder. The variable d is the speed rate in Gaussian surface.)
2) Execute main.py.(Notice: the python version: python36)
3) After the main.py is ended, the output .txt file is under the \output directory.

------------------------------------------------------------------------------------------------------------------------ 
A quick guide for usage of this version:
command line style:

cd example

python3 main.py xxx.pqr d

(Notice: the pqr file should be put in the folder named "pqr". The output .txt file is in the folder named "output". )

Example: python3 main.py adp.pqr 0.5

------------------------------------------------------------------------------------------------------------------------
 You may contact Dr. Sheng Gui, email: shenggui@lsec.cc.ac.cn or Ms. Zhaodi Chen, email: 20174207022@stu.suda.edu.cn, if you have any problem running this program.
   

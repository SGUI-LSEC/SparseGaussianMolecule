import sys
import time
import sparseMolecule

def main(pqrfile,d_para):
    sparseMolecule.sparseMolecule(pqrfile,d_para)

if __name__ == '__main__':
    pqrfile = sys.argv[1]
    d_para = sys.argv[2]
    main(pqrfile,d_para)


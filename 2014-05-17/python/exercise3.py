""" progressive refinement of a block diagram """
from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, 'C:\Python27\Lib\site-packages\larcc\lib\py')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *
from architectural import *
from splines import *


def MNE (shape,sizePattern,master,k):
	V,CV = master
	celle_master = len(CV)-1
	celle_scritte = []
	toRemove = []

	diagram = assemblyDiagramInit(shape)(sizePattern)
	master = diagram2cell(diagram,master,k)

	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
	VIEW(hpc)

	end = True 
	while (end):
		selezione = input('Inserisci il numero delle celle da rimuovere (digita -1 se vuoi terminare): ')
		celle_scritte.append(selezione)
		if (selezione == -1):
			end = False

	toRemove = celle_scritte
	master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
	DRAW(master)

#test di verifica
DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),YELLOW,1)
VIEW(hpc)

toRemove = [13,33,17,37]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
VIEW(hpc)

MNE([3,1,2],[[2,1,2],[.3],[2.2,.5]],master,29)

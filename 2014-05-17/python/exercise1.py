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

DRAW = COMP([VIEW,STRUCT,MKPOLS])

shape =[9,7,2]
sizePattern=[[.3,1.8,.1,1.2,.1,.6,.1,.7,.3],[.3,.8,.1,.8,.1,1.2,.3],[.3,2.7]]
master = assemblyDiagramInit(shape)(sizePattern)
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),YELLOW,1)
#VIEW(hpc)

toRemove = [17,19,21,25,45,49,51,53,73,87,107,77,91,101,81,109,105,101]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toMerge=39
p1 = assemblyDiagramInit([3,1,2])([[0.3,0.6,0.3],[.3],[1.5,1]])
master = diagram2cell(p1,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toRemove = [110]
diagram = master[0], [cell for k,cell in enumerate(master[1]) if (k in toRemove)]
hpcp1 = COLOR([0.8,0.5,0.2])((STRUCT(MKPOLS(diagram))))
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,1)
#VIEW(hpc)

toMerge=3
f1 = assemblyDiagramInit([1,3,3])([[.3],[.2,.4,.2],[1.2,.6,.9]])
hpcf1 = COLOR([0,0.48,0.65])((STRUCT(MKPOLS(f1))))
master = diagram2cell(f1,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=6
f2 = assemblyDiagramInit([1,3,3])([[.3],[.2,.4,.2],[1.2,.6,.9]])
master = diagram2cell(f2,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=9
f3 = assemblyDiagramInit([1,3,3])([[.3],[.4,.4,.4],[1.2,.6,.9]])
master = diagram2cell(f3,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toRemove = [114,123,132]
diagram = master[0], [cell for k,cell in enumerate(master[1]) if (k in toRemove)]
hpcf1 = COLOR([0,0.48,0.65])((STRUCT(MKPOLS(diagram))))
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge=20
f4 = assemblyDiagramInit([3,1,3])([[.7,.4,.7],[.3],[1.2,.6,.9]])
master = diagram2cell(f4,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=42
f5 = assemblyDiagramInit([3,1,3])([[.4,.4,.4],[.3],[1.2,.6,.9]])
master = diagram2cell(f5,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=66
f6 = assemblyDiagramInit([3,1,3])([[.3,.3,.3],[.3],[1.2,.6,.9]])
master = diagram2cell(f6,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=87
f7 = assemblyDiagramInit([3,1,3])([[.2,.3,.2],[.3],[1.2,.6,.9]])
master = diagram2cell(f7,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toRemove = [134,143,152,161]
diagram = master[0], [cell for k,cell in enumerate(master[1]) if (k in toRemove)]
hpcf2 = COLOR([0,0.48,0.65])((STRUCT(MKPOLS(diagram))))
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge=90
f8 = assemblyDiagramInit([1,3,3])([[.3],[.2,.4,.2],[1.2,.6,.9]])
master = diagram2cell(f8,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toRemove = [165]
diagram = master[0], [cell for k,cell in enumerate(master[1]) if (k in toRemove)]
hpcf3 = COLOR([0,0.48,0.65])((STRUCT(MKPOLS(diagram))))
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge=37
p2 = assemblyDiagramInit([3,1,2])([[.3,.6,.3],[.3],[1.5,1]])
master = diagram2cell(p2,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=31
p3 = assemblyDiagramInit([1,3,2])([[.3],[.3,.6,.3],[1.5,1]])
master = diagram2cell(p3,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=23
p4 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p4,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=26
p5 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p5,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=41
p6 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p6,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=44
p7 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p7,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toMerge=47
p8 = assemblyDiagramInit([1,3,2])([[.3],[.2,.6,.4],[1.5,1]])
master = diagram2cell(p8,master,toMerge)
#hpc = SKEL_1(STRUCT(MKPOLS(master)))
#hpc = cellNumbering (master,hpc)(range(len(master[1])),YELLOW,0.25)
#VIEW(hpc)

toRemove = [164,176,188,182,170,200,194]
diagram = master[0], [cell for k,cell in enumerate(master[1]) if (k in toRemove)]
hpcp2 = COLOR([0.8,0.5,0.2])((STRUCT(MKPOLS(diagram))))
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)

hpcs = COLOR([0.82,0.71,0.55])(STRUCT(MKPOLS(master)))

hpc=STRUCT([hpcp1,hpcf1,hpcf2,hpcf2,hpcf3,hpcp2,hpcs])
VIEW(hpc)

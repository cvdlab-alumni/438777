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
from mapper import *
from splines import *
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
masterCasaA=master
#DRAW(master) #solo finestre a destra

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
masterCasaB=master
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
#DRAW(master)

hpcs = COLOR([0.82,0.71,0.55])(STRUCT(MKPOLS(master)))

hpc=STRUCT([hpcp1,hpcf1,hpcf2,hpcf2,hpcf3,hpcp2,hpcs])
#VIEW(hpc) #casetta colorata finale

"""esercizo2"""

palazzo = assemblyDiagramInit([3,9,7])([[5.2,4,.3],[1,4.6,1,4.6,6,1,4.6,1,4.6],[1,3,1,3,1,3,1]])
V,CV = palazzo

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(CV)),YELLOW,1)
#VIEW(hpc)

palazzo = diagram2cell(masterCasaB,palazzo,61)
palazzo = diagram2cell(masterCasaB,palazzo,59)
palazzo = diagram2cell(masterCasaB,palazzo,57)
palazzo = diagram2cell(masterCasaA,palazzo,47)
palazzo = diagram2cell(masterCasaA,palazzo,45)
palazzo = diagram2cell(masterCasaA,palazzo,43)
palazzo = diagram2cell(masterCasaB,palazzo,26)
palazzo = diagram2cell(masterCasaB,palazzo,24)
palazzo = diagram2cell(masterCasaB,palazzo,22)
palazzo = diagram2cell(masterCasaA,palazzo,12)
palazzo = diagram2cell(masterCasaA,palazzo,10)
palazzo = diagram2cell(masterCasaA,palazzo,8)

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(CV)),RED,1)
#VIEW(hpc)

toRemove =[6,57,120,10,17,21,28,85,78,71,64,85,39,99,162,169,106,46,113,50,176,183,155,148,141,134,127,92,68,61,35]
palazzo = palazzo[0],[cell for k,cell in enumerate(palazzo[1]) if not (k in toRemove)]
hpc = STRUCT(MKPOLS(palazzo))
#VIEW(hpc)
#DRAW(palazzo) #senza tetto

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(CV)),RED,1)
#VIEW(hpc)

toRemove =[23,22,21,20,19,18]
palazzo = palazzo[0],[cell for k,cell in enumerate(palazzo[1]) if not (k in toRemove)]
hpc = STRUCT(MKPOLS(palazzo))
#VIEW(hpc)
#DRAW(palazzo) #struttura definita

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(CV)),RED,1)
#VIEW(hpc)

#58-63
"""
toMerge=58
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=60
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=62
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
"""
toMerge=59
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=60
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=61
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=60
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=59
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=58
diagram = assemblyDiagramInit([3,5,1])([[.3,1.2,2.5],[.2,2.5,.6,2.5,.2],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(palazzo[1])),RED,1)
#VIEW(hpc)

toRemove =[1999,1997,1988,1984,1982,1969,1967,1954,1952,1939,1937,1924,1922]
palazzo = palazzo[0],[cell for k,cell in enumerate(palazzo[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
#DRAW(palazzo) #palazzo buchi ascensore,scale e porta anteriore

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(palazzo[1])),RED,1)
#VIEW(hpc)

toMerge=0
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=0
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=0
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=0
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=0
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=0
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

toMerge=3
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=3
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=3
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=3
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=3
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=3
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

toMerge=6
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=6
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=6
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=6
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=6
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=6
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

toMerge=9
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=9
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=9
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=9
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=9
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=9
diagram = assemblyDiagramInit([2,1,1])([[.3,4.9],[1],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

toMerge=1965
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1966
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1967
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1968
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1969
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1970
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

toMerge=1983
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1984
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1985
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1986
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1987
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=1988
diagram = assemblyDiagramInit([1,2,1])([[5.2],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

toMerge=12
diagram = assemblyDiagramInit([1,2,1])([[4],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=12
diagram = assemblyDiagramInit([1,2,1])([[4],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=12
diagram = assemblyDiagramInit([1,2,1])([[4],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=12
diagram = assemblyDiagramInit([1,2,1])([[4],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=12
diagram = assemblyDiagramInit([1,2,1])([[4],[.3,.7],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=12
diagram = assemblyDiagramInit([1,2,1])([[4],[.3,.7],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

toMerge=46
diagram = assemblyDiagramInit([1,2,1])([[4],[4.3,.3],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=46
diagram = assemblyDiagramInit([1,2,1])([[4],[4.3,.3],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=46
diagram = assemblyDiagramInit([1,2,1])([[4],[4.3,.3],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=46
diagram = assemblyDiagramInit([1,2,1])([[4],[4.3,.3],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=46
diagram = assemblyDiagramInit([1,2,1])([[4],[4.3,.3],[1]])
palazzo = diagram2cell(diagram,palazzo,toMerge)
toMerge=46
diagram = assemblyDiagramInit([1,2,1])([[4],[4.3,.3],[3]])
palazzo = diagram2cell(diagram,palazzo,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(palazzo[1])),RED,1)
#VIEW(hpc) #definiti bordi palazzo

toRemove =[2034,2030,2026,2023,2019,2015,2011,2007,2003,1999,1995,1991,1987,1983,1979,1969,1965,1961,1913,1912,1911,1910,1909,1908,1907,1906,
1900,1899,1898,1897,1896,1895,1894,1893,1887,1886,1885,1884,1883,1882,1881,1880,45,43,41,39,37,35,33,31,29,27,25,23,21,19,17,16,13]
palazzo = palazzo[0],[cell for k,cell in enumerate(palazzo[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
#VIEW(hpc)
#DRAW(palazzo) #corridoi piani

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(palazzo[1])),RED,1)
#VIEW(hpc)

restauro = assemblyDiagramInit([1,1,1])([[.3],[.6],[1]])
restauro = larApply( t(5.2,13.9,0) )(restauro)

scaleAnteriori=assemblyDiagramInit([4,1,4])([4*[.5],[.6],4*[.25]])
hpc = SKEL_1(STRUCT(MKPOLS(scaleAnteriori)))
hpc = cellNumbering (scaleAnteriori,hpc)(range(len(scaleAnteriori[1])),CYAN,2)
toRemove =[11,7,6,3,2,1]
scaleAnteriori = scaleAnteriori[0],[cell for k,cell in enumerate(scaleAnteriori[1]) if not (k in toRemove)]

scaleSud = larApply(r(0,0,PI/2))(scaleAnteriori)
scaleSud = larApply( t(7.5,-2,0) )(scaleSud)

scaleNord = larApply(r(0,0,PI))(scaleSud)
scaleNord = larApply( t(14.4,28.4,0) )(scaleNord)

scaleAnteriori = larApply( t(3.2,13.9,0))(scaleAnteriori)

scalePosteriori=assemblyDiagramInit([4,1,4])([4*[.5],[.6],4*[.25]])
hpc = SKEL_1(STRUCT(MKPOLS(scalePosteriori)))
hpc = cellNumbering (scalePosteriori,hpc)(range(len(scalePosteriori[1])),CYAN,2)
toRemove =[15,14,13,11,10,7]
scalePosteriori = scalePosteriori[0],[cell for k,cell in enumerate(scalePosteriori[1]) if not (k in toRemove)]
scalePosteriori = larApply( t(9.5,13.9,0))(scalePosteriori)

ascensore=assemblyDiagramInit([2,3,9])([[.3,2],[.85,.6,.85],[1,2,1,1,2,1,1,2,1]])
hpc = SKEL_1(STRUCT(MKPOLS(ascensore)))
hpc = cellNumbering (ascensore,hpc)(range(len(ascensore[1])),CYAN,2)
toRemove =[16,13,10]
ascensore = ascensore[0],[cell for k,cell in enumerate(ascensore[1]) if not (k in toRemove)]
ascensore = larApply( t(6.8,14.6,0))(ascensore)

scalaInterna=assemblyDiagramInit([1,2,12])([[2.5],[1.25,1.25],[1.8,0.4,1.8,0.4,1.8,0.4,1.8,0.4,1.8,0.4,1.8,0.4]])
#2,0.5,2,0.5,2,0.5,2,0.5,2,0.5,2,0.5
hpc = SKEL_1(STRUCT(MKPOLS(scalaInterna)))
hpc = cellNumbering (scalaInterna,hpc)(range(len(scalaInterna[1])),CYAN,2)

scalaInterna = diagram2cell(scalePosteriori,scalaInterna,22)
scalaInterna = diagram2cell(scalePosteriori,scalaInterna,18)
scalaInterna = diagram2cell(scalePosteriori,scalaInterna,14)
scalaInterna = diagram2cell(scaleAnteriori,scalaInterna,8)
scalaInterna = diagram2cell(scaleAnteriori,scalaInterna,4)
scalaInterna = diagram2cell(scaleAnteriori,scalaInterna,0)
hpc = SKEL_1(STRUCT(MKPOLS(scalaInterna)))
hpc = cellNumbering (scalaInterna,hpc)(range(len(scalaInterna[1])),CYAN,2)
#VIEW(hpc)

supportoScala1=assemblyDiagramInit([1,1,2])([[1],[1],[2,1]])
supportoScala2=assemblyDiagramInit([2,2,1])([[2,.7],[1,.5],[1]])
supportoScala3=assemblyDiagramInit([2,2,1])([[2,.7],[.5,1],[1]])
supportoScala4=assemblyDiagramInit([2,2,1])([[.7,2],[.5,1],[1]])
supportoScala5=assemblyDiagramInit([2,2,1])([[.7,2],[1,.5],[1]])

scalaInterna = diagram2cell(supportoScala4,scalaInterna,17)
scalaInterna = diagram2cell(supportoScala3,scalaInterna,16)
scalaInterna = diagram2cell(supportoScala1,scalaInterna,15)
scalaInterna = diagram2cell(supportoScala4,scalaInterna,14)
scalaInterna = diagram2cell(supportoScala3,scalaInterna,13)
scalaInterna = diagram2cell(supportoScala1,scalaInterna,12)
scalaInterna = diagram2cell(supportoScala4,scalaInterna,11)
scalaInterna = diagram2cell(supportoScala3,scalaInterna,10)
scalaInterna = diagram2cell(supportoScala1,scalaInterna,7)
scalaInterna = diagram2cell(supportoScala2,scalaInterna,6)
scalaInterna = diagram2cell(supportoScala5,scalaInterna,5)
scalaInterna = diagram2cell(supportoScala1,scalaInterna,4)
scalaInterna = diagram2cell(supportoScala2,scalaInterna,3)
scalaInterna = diagram2cell(supportoScala5,scalaInterna,2)
scalaInterna = diagram2cell(supportoScala1,scalaInterna,1)
scalaInterna = diagram2cell(supportoScala2,scalaInterna,0)

hpc = SKEL_1(STRUCT(MKPOLS(scalaInterna)))
hpc = cellNumbering (scalaInterna,hpc)(range(len(scalaInterna[1])),YELLOW,1)
#VIEW(hpc)

toRemove =[114,113,112,110,104,103,102,100,99,98,97,96,95,94,93,92,91,90,
           75,74,73,72,71,70,69,68,67,66,65,64,63,62,85,84,83,80,41,40,39,38,37,36,35,34,33,32,11,10,9,8,7,6,5,4,3,2,1,0]
scalaInterna = scalaInterna[0],[cell for k,cell in enumerate(scalaInterna[1]) if not (k in toRemove)]
scalaInterna = larApply( t(6.7,11.4,0))(scalaInterna)

#muretto esterno
controlpoints = [[0,0],[0,2],[2,2],[4,2],[4,0]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
wallEst = STRUCT(MKPOLS(obj))
#muretto interno
controlpoints = [[.1,0],[.1,1.9],[1.8,1.8],[3.9,1.9],[3.9,0]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
wallInt = STRUCT(MKPOLS(obj))
#tutto
muretto = STRUCT([wallEst,wallInt,POLYLINE([[0,0],[.1,0]]),POLYLINE([[3.8,0],[4,0]])])
muro = PROD([SOLIDIFY(muretto),Q(1)])
giardino = SOLIDIFY(STRUCT([wallInt,POLYLINE([[.1,0],[3.9,0]])]))
giardinoNord = STRUCT([COLOR([.98,.87,.68])(muro),COLOR([.59,.46,.33])(giardino)])

balcone1=T([1,2,3])([5.5,28.4,5])(giardinoNord)
balcone2=T(3)(4)(balcone1)

latoNord=STRUCT([balcone1,balcone2])

#muretto esterno
controlpoints = [[0,0],[0,-2],[2,-2],[4,-2],[4,0]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
wallEst = STRUCT(MKPOLS(obj))
#muretto interno
controlpoints = [[.1,0],[.1,-1.9],[1.8,-1.8],[3.9,-1.9],[3.9,0]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
wallInt = STRUCT(MKPOLS(obj))
#tutto
muretto = STRUCT([wallEst,wallInt,POLYLINE([[0,0],[.1,0]]),POLYLINE([[3.8,0],[4,0]])])
muro = PROD([SOLIDIFY(muretto),Q(1)])
giardino = SOLIDIFY(STRUCT([wallInt,POLYLINE([[.1,0],[3.9,0]])]))
giardinoSud = STRUCT([COLOR([.98,.87,.68])(muro),COLOR([.59,.46,.33])(giardino)])

balcone1=T([1,3])([5.5,5])(giardinoSud)
balcone2=T(3)(4)(balcone1)

latoSud=STRUCT([balcone1,balcone2])

#muretto esterno
controlpoints = [[9.5,28.4],[24.5,28.4],[24.5,14.2],[24.5,0],[9.5,0]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
wallEst = STRUCT(MKPOLS(obj))
#muretto interno
controlpoints = [[9.5,28.3],[24.4,28.3],[24.4,14.1],[24.4,.1],[9.5,.1]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
wallInt = STRUCT(MKPOLS(obj))
#tutto
muretto = STRUCT([wallEst,wallInt,POLYLINE([[9.5,28.4],[9.5,28.3]]),POLYLINE([[9.5,0],[9.5,.1]])])
muro = PROD([SOLIDIFY(muretto),Q(.75)])
giardino = SOLIDIFY(STRUCT([wallInt,POLYLINE([[9.5,28.3],[9.5,.1]])]))
giardinoEst = STRUCT([COLOR([.98,.87,.68])(muro),COLOR([0,0.69,0.42])(giardino)])

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(palazzo[1])),YELLOW,1)
#VIEW(hpc)

toMerge=1860
portaAnteriore=assemblyDiagramInit([1,1,2])([[.3],[.6],[2,1]])
palazzo = diagram2cell(portaAnteriore,palazzo,toMerge)

toMerge=54
portaPosteriore=assemblyDiagramInit([1,3,2])([[.3],[2.7,.6,2.7],[2,1]])
palazzo = diagram2cell(portaPosteriore,palazzo,toMerge)

portaBalcone=assemblyDiagramInit([3,1,2])([[1.7,.6,1.7],[.3],[2,1]])
palazzo = diagram2cell(portaBalcone,palazzo,1974)
palazzo = diagram2cell(portaBalcone,palazzo,1971)
palazzo = diagram2cell(portaBalcone,palazzo,1968)
palazzo = diagram2cell(portaBalcone,palazzo,1965)
palazzo = diagram2cell(portaBalcone,palazzo,1962)
palazzo = diagram2cell(portaBalcone,palazzo,1959)

hpc = SKEL_1(STRUCT(MKPOLS(palazzo)))
hpc = cellNumbering (palazzo,hpc)(range(len(palazzo[1])),YELLOW,1)
#VIEW(hpc)

toRemove =[2009,2003,1997,1991,1985,1979,1973,1969,15]
diagram = palazzo[0], [cell for k,cell in enumerate(palazzo[1]) if (k in toRemove)]
porte = COLOR([.59,.46,.33])((STRUCT(MKPOLS(diagram))))
palazzo = palazzo[0],[cell for k,cell in enumerate(palazzo[1]) if not (k in toRemove)]

restauroBis = assemblyDiagramInit([1,1,1])([[2.5],[2.5],[1]])
restauroBis = larApply( t(6.7,11.4,0) )(restauroBis)
restauroTer = assemblyDiagramInit([1,1,1])([[4],[1],[1]])
restauroTer = larApply( t(5.2,5.6,0) )(restauroTer)
restauroQuater = assemblyDiagramInit([1,1,1])([[2.5],[1.25],[2]])
restauroQuater = larApply( t(6.7,12.65,0) )(restauroQuater)
restauroQuinquies = assemblyDiagramInit([1,1,1])([[4],[1],[1]])
restauroQuinquies = larApply( t(5.2,5.6,4) )(restauroQuinquies)

COLOR([0.82,0.71,0.55])(STRUCT(MKPOLS(master)))
casa = Struct([palazzo,restauro,restauroBis,restauroTer,restauroQuater,restauroQuinquies,scaleAnteriori,scalePosteriori,ascensore,scalaInterna,scaleSud,scaleNord])
casaLar=STRUCT(CAT(AA(MKPOLS)(casa)))
#VIEW(casaLar)
#VIEW(STRUCT([casaLar,latoNord,latoSud,giardinoEst])) #palazzo modello larcc misto plasm

palazzo=COLOR([.98,.87,.68])(STRUCT(MKPOLS(palazzo)))
restauro=COLOR([.98,.87,.68])(STRUCT(MKPOLS(restauro)))
restauroBis=COLOR([.98,.87,.68])(STRUCT(MKPOLS(restauroBis)))
restauroTer=COLOR([.98,.87,.68])(STRUCT(MKPOLS(restauroTer)))
restauroQuater=COLOR([.59,.46,.33])(STRUCT(MKPOLS(restauroQuater)))
restauroQuinquies=COLOR([.98,.87,.68])(STRUCT(MKPOLS(restauroQuinquies)))
scaleAnteriori=COLOR([.59,.46,.33])(STRUCT(MKPOLS(scaleAnteriori)))
scalePosteriori=COLOR([.59,.46,.33])(STRUCT(MKPOLS(scalePosteriori)))
ascensore=COLOR([.85,.74,.67])(STRUCT(MKPOLS(ascensore)))
scalaInterna=COLOR([.59,.46,.33])(STRUCT(MKPOLS(scalaInterna)))
scaleSud=COLOR([.59,.46,.33])(STRUCT(MKPOLS(scaleSud)))
scaleNord=COLOR([.59,.46,.33])(STRUCT(MKPOLS(scaleNord)))

finestra=assemblyDiagramInit([1,1,1])([[.3],[.5],[.6]])

f1 = larApply( t(0,1.65,2.5))(finestra)
f2 = larApply( t(0,1.15,0))(f1)
f3 = larApply( t(0,1.4,0))(f2)
f4 = larApply( t(0,0,4))(f1)
f5 = larApply( t(0,0,4))(f2)
f6 = larApply( t(0,0,4))(f3)
f7 = larApply( t(0,0,4))(f4)
f8 = larApply( t(0,0,4))(f5)
f9 = larApply( t(0,0,4))(f6)
f1=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f1)))
f2=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f2)))
f3=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f3)))
f4=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f4)))
f5=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f5)))
f6=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f6)))
f7=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f7)))
f8=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f8)))
f9=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f9)))
finPrimoBlocco=STRUCT([f1,f2,f3,f4,f5,f6,f7,f8,f9])
finSecondoBlocco=T(2)(5.6)(finPrimoBlocco)
finSud=STRUCT([finPrimoBlocco,finSecondoBlocco])

finTerzoBlocco=T(2)(17.2)(finSud)
finestreSuY=STRUCT([finSud,finTerzoBlocco])

finestra=assemblyDiagramInit([1,1,1])([[.4],[.3],[.6]])
f1 = larApply( t(1,10.9,2.5))(finestra)
f2 = larApply( t(0,0,4))(f1)
f3 = larApply( t(0,0,4))(f2)
f1=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f1)))
f2=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f2)))
f3=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f3)))

finPrimoBlocco=STRUCT([f1,f2,f3])
finSeconBlocco=T(1)(1.6)(finPrimoBlocco)

finestra2=assemblyDiagramInit([1,1,1])([[.2],[.3],[.6]])
f4 = larApply( t(3.7,10.9,2.5))(finestra2)
f6 = larApply( t(0,0,4))(f4)
f7 = larApply( t(0,0,4))(f6)
f4=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f4)))
f6=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f6)))
f7=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f7)))

finestra3=assemblyDiagramInit([1,1,1])([[.3],[.3],[.6]])
f5 = larApply( t(4.4,10.9,2.5))(finestra3)
f8 = larApply( t(0,0,4))(f5)
f9 = larApply( t(0,0,4))(f8)
f5=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f5)))
f8=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f8)))
f9=COLOR([0,0.48,0.65])(STRUCT(MKPOLS(f9)))

fin=STRUCT([f4,f5,f6,f7,f8,f9,finPrimoBlocco,finSeconBlocco])
finestreSuX=STRUCT([fin,T(2)(17.2)(fin)])

VIEW(STRUCT([latoNord,latoSud,giardinoEst,palazzo,restauro,restauroBis,restauroTer,restauroQuater,restauroQuinquies,scaleAnteriori,scalePosteriori,
             ascensore,scalaInterna,scaleSud,scaleNord,porte,finestreSuY,finestreSuX]))





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

toRemove = [17,19,21,25,45,49,51,53,73,87,107,77,91,101,81,109,105,101]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

toMerge=39
p1 = assemblyDiagramInit([3,1,2])([[0.3,0.6,0.3],[.3],[1.5,1]])
master = diagram2cell(p1,master,toMerge)

toRemove = [110]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge=3
f1 = assemblyDiagramInit([1,3,3])([[.3],[.2,.4,.2],[1.2,.6,.9]])
master = diagram2cell(f1,master,toMerge)

toMerge=6
f2 = assemblyDiagramInit([1,3,3])([[.3],[.2,.4,.2],[1.2,.6,.9]])
master = diagram2cell(f2,master,toMerge)

toMerge=9
f3 = assemblyDiagramInit([1,3,3])([[.3],[.4,.4,.4],[1.2,.6,.9]])
master = diagram2cell(f3,master,toMerge)

toRemove = [114,123,132]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge=20
f4 = assemblyDiagramInit([3,1,3])([[.7,.4,.7],[.3],[1.2,.6,.9]])
master = diagram2cell(f4,master,toMerge)

toMerge=42
f5 = assemblyDiagramInit([3,1,3])([[.4,.4,.4],[.3],[1.2,.6,.9]])
master = diagram2cell(f5,master,toMerge)

toMerge=66
f6 = assemblyDiagramInit([3,1,3])([[.3,.3,.3],[.3],[1.2,.6,.9]])
master = diagram2cell(f6,master,toMerge)

toMerge=87
f7 = assemblyDiagramInit([3,1,3])([[.2,.3,.2],[.3],[1.2,.6,.9]])
master = diagram2cell(f7,master,toMerge)

toRemove = [134,143,152,161]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge=90
f8 = assemblyDiagramInit([1,3,3])([[.3],[.2,.4,.2],[1.2,.6,.9]])
master = diagram2cell(f8,master,toMerge)

toRemove = [165]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge=37
p2 = assemblyDiagramInit([3,1,2])([[.3,.6,.3],[.3],[1.5,1]])
master = diagram2cell(p2,master,toMerge)

toMerge=31
p3 = assemblyDiagramInit([1,3,2])([[.3],[.3,.6,.3],[1.5,1]])
master = diagram2cell(p3,master,toMerge)

toMerge=23
p4 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p4,master,toMerge)

toMerge=26
p5 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p5,master,toMerge)

toMerge=41
p6 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p6,master,toMerge)

toMerge=44
p7 = assemblyDiagramInit([1,3,2])([[.3],[.1,.6,.1],[1.5,1]])
master = diagram2cell(p7,master,toMerge)

toMerge=47
p8 = assemblyDiagramInit([1,3,2])([[.3],[.2,.6,.4],[1.5,1]])
master = diagram2cell(p8,master,toMerge)

toRemove = [164,176,188,182,170,200,194]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

"esercizio2"
palazzo = assemblyDiagramInit([3,4,4])([[5.2,3,5.2],[1,4.6,1,4.6],4*[3.2]])
V,CV = palazzo

palazzo = diagram2cell(master,palazzo,47)
palazzo = diagram2cell(master,palazzo,46)
palazzo = diagram2cell(master,palazzo,45)
palazzo = diagram2cell(master,palazzo,44)
palazzo = diagram2cell(master,palazzo,39)
palazzo = diagram2cell(master,palazzo,38)
palazzo = diagram2cell(master,palazzo,37)
palazzo = diagram2cell(master,palazzo,36)
palazzo = diagram2cell(master,palazzo,15)
palazzo = diagram2cell(master,palazzo,14)
palazzo = diagram2cell(master,palazzo,13)
palazzo = diagram2cell(master,palazzo,12)
palazzo = diagram2cell(master,palazzo,7)
palazzo = diagram2cell(master,palazzo,6)
palazzo = diagram2cell(master,palazzo,5)
palazzo = diagram2cell(master,palazzo,4)

toRemove = [31,27,23,19,15,11,7,3]
palazzo = palazzo[0],[cell for k,cell in enumerate(palazzo[1]) if not (k in toRemove)]
hpc = STRUCT(MKPOLS(palazzo))

palazzo=(T(3)(2)(hpc))

c1=CYLINDER([0.4,2])(40)
c1=T([1,2])([.3,.3])(c1)
c2=CYLINDER([0.4,2])(40)
c2=T([1,2])([.3,10.9])(c2)
c3=CYLINDER([0.4,2])(40)
c3=T([1,2])([13.1,.3])(c3)
c4=CYLINDER([0.4,2])(40)
c4=T([1,2])([13.1,10.9])(c4)

c5=CYLINDER([0.4,2])(40)
c5=T([1,2])([.3,4.3])(c5)
c6=CYLINDER([0.4,2])(40)
c6=T([1,2])([.3,6.9])(c6)
c7=CYLINDER([0.4,2])(40)
c7=T([1,2])([4.3,10.9])(c7)
c8=CYLINDER([0.4,2])(40)
c8=T([1,2])([6.7,10.9])(c8)
c9=CYLINDER([0.4,2])(40)
c9=T([1,2])([9.1,10.9])(c9)
c10=CYLINDER([0.4,2])(40)
c10=T([1,2])([13.1,6.9])(c10)
c11=CYLINDER([0.4,2])(40)
c11=T([1,2])([13.1,4.3])(c11)
c12=CYLINDER([0.4,2])(40)
c12=T([1,2])([9.1,.3])(c12)
c13=CYLINDER([0.4,2])(40)
c13=T([1,2])([4.3,.3])(c13)

pilastri=STRUCT([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13])

assembly1=STRUCT([COLOR([1,0.8,0.6])(palazzo),COLOR([0.804,0.361,0.361])(pilastri)])

controls11 = [[.3,.3],[1.2,-.3],[.3,-1.8]]
bezier11 = BEZIER(S1)(controls11)

controls12 = [[.3,-1.8],[-1.5,-1.5],[-1.8,.3],[.3,.3]]
bezier12 = BEZIER(S1)(controls12)

base1=MAP(BEZIER(S2)([bezier11,bezier12]))(POWER([INTERVALS(1)(30),INTERVALS(1)(30)]))

controls21 = [[13.1,10.9],[15.2,10.9],[14.9,12.7],[12.8,12.7]]
bezier21 = BEZIER(S1)(controls21)

controls22 = [[12.8,12.7],[11.9,11.5],[13.1,10.9]]
bezier22 = BEZIER(S1)(controls22)

base2=MAP(BEZIER(S2)([bezier21,bezier22]))(POWER([INTERVALS(1)(30),INTERVALS(1)(30)]))

controls31 = [[13.1,.3],[14,1.8],[15.5,.6],[15.2,-1.2]]
bezier31 = BEZIER(S1)(controls31)

controls32 = [[15.2,-1.2],[13.1,-1.5],[13.1,.3]]
bezier32 = BEZIER(S1)(controls32)

base3=MAP(BEZIER(S2)([bezier31,bezier32]))(POWER([INTERVALS(1)(30),INTERVALS(1)(30)]))

controls41 = [[.3,10.9],[1.5,11.5],[.6,12.4],[-1.5,12.7]]
bezier41 = BEZIER(S1)(controls41)

controls42 = [[-1.5,12.7],[-1.2,10.9],[.3,10.9]]
bezier42 = BEZIER(S1)(controls42)

base4=MAP(BEZIER(S2)([bezier41,bezier42]))(POWER([INTERVALS(1)(30),INTERVALS(1)(30)]))

controls6 = [[-10,8],[-12,25],[15,23],[26,24],[23,19]]
bezier6 = BEZIER(S1)(controls6)

controls5 = [[23,19],[24,-15],[20,-14],[21,-16],[-13,-16],[-10,8]]
bezier5 = BEZIER(S1)(controls5)

base=MAP(BEZIER(S2)([bezier6,bezier5]))(POWER([INTERVALS(1)(30),INTERVALS(1)(30)]))

assembly2=STRUCT([T(3)(0.01)(COLOR([0.09,0.51,0.27])(base1))]+[T(3)(0.01)(COLOR([0.09,0.51,0.27])(base2))]+[T(3)(0.01)(COLOR([0.09,0.51,0.27])(base3))]+[T(3)(0.01)(COLOR([0.09,0.51,0.27])(base4))]+[COLOR([0,0.66,0.42])(base)]+[assembly1])

scala=STRUCT(MKPOLS(spiralStair(0.1)))
scala=T([1,2])([6,0])(COLOR([0.804,0.361,0.361])(scala))
portaPrincipale=T([1,2,3])([6.25,-0.01,2])(COLOR([0.804,0.361,0.361])(CUBOID([1,.3,2.5])))

tronco=COLOR([0.588,0.294,0])(CYLINDER([0.2,6])(40))
chioma=COLOR([0.133,0.545,0.133,100])(T(3)(6)((SPHERE(1)([20,20]))))
albero=STRUCT([tronco,chioma])

a1=T([1,2])([-.7,-.7])(albero)
a2=T([1,2])([14.1,-.7])(albero)
a3=T([1,2])([14.1,11.9])(albero)
a4=T([1,2])([-.7,11.9])(albero)

alberi=STRUCT([a1,a2,a3,a4])

assembly3=STRUCT([assembly2,scala,portaPrincipale,alberi])
VIEW(SKEL_1(assembly3))
VIEW(assembly3)


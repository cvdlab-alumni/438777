from pyplasm import *

def circle(r):
	def circle0(p):
		alpha= p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

def colonna(p):
		x,y=p
		plinto_a=(CIRCUMFERENCE(0.5)(80))
		pa=T([1,2])([x,y])(plinto_a)
		pl_a=PROD([pa,Q(0.2)])
		base=SKELETON(1)(STRUCT([T([1,2])([x,y])(CIRCUMFERENCE(0.3)(80))]))
		pilastro=PROD([base,Q(4)])
		return COLOR([1,0.8,0.6])(SKELETON(1)(STRUCT([pl_a,pilastro])))

obj = MAP(circle(7.4))(INTERVALS(2*PI)(32))
obj2 = MAP(circle(7.6))(INTERVALS(2*PI)(32))
obj3 = MAP(circle(7.8))(INTERVALS(2*PI)(32))
obj4 = MAP(circle(8.0))(INTERVALS(2*PI)(32))
obj5 = MAP(circle(8.2))(INTERVALS(2*PI)(32))
obj6 = MAP(circle(8.4))(INTERVALS(2*PI)(32))
obj7 = MAP(circle(8.6))(INTERVALS(2*PI)(32))

scalini=COLOR([0.804,0.498,0.196])(STRUCT([obj,obj2,obj3,obj4,obj5,obj6,obj7]))
scalini=(T([1,2])([10,10])(scalini))

cella_ax = MAP(circle(4))(INTERVALS(0.9*PI)(32))
c_ax = PROD([cella_ax,Q(4)])
cella_bx = R([1,2])(1.1*PI)(MAP(circle(4))(INTERVALS(0.9*PI)(32)))
c_bx = PROD([cella_bx,Q(4)])
cella_x=COLOR([0.698,0,0])(SKELETON(1)(STRUCT([c_ax,c_bx])))

cella_ay = MAP(circle(3.8))(INTERVALS(0.9*PI)(32))
c_ay = PROD([cella_ay,Q(4)])
cella_by = R([1,2])(1.1*PI)(MAP(circle(3.8))(INTERVALS(0.9*PI)(32)))
c_by = PROD([cella_by,Q(4)])
cella_y=COLOR([0.698,0,0])(STRUCT([c_ay,c_by]))

cella=COLOR([0.698,0,0])(T([1,2])([10,10])(STRUCT([cella_x,cella_y])))
#VIEW(T([1,2])(10)(STRUCT([scalini,cella]))) //scalini+cella

trab_a = COLOR([0.722,0.451,0.2])(MAP(circle(6))(INTERVALS(2*PI)(32)))
trab_b = COLOR([0.722,0.451,0.2])(MAP(circle(6.4))(INTERVALS(2*PI)(32)))
trabeazione=T([1,2])([10,10])(STRUCT([trab_a,trab_b]))

listaPunti=CIRCLE_POINTS(6.2,20)
c=colonna(listaPunti[0])
c1=colonna(listaPunti[1])
c3=colonna(listaPunti[2])
c4=colonna(listaPunti[3])
c5=colonna(listaPunti[4])
c6=colonna(listaPunti[5])
c7=colonna(listaPunti[6])
c8=colonna(listaPunti[7])
c9=colonna(listaPunti[8])
c10=colonna(listaPunti[9])
c11=colonna(listaPunti[10])
c12=colonna(listaPunti[11])
c13=colonna(listaPunti[12])
c14=colonna(listaPunti[13])
c15=colonna(listaPunti[14])
c16=colonna(listaPunti[15])
c17=colonna(listaPunti[16])
c18=colonna(listaPunti[17])
c19=colonna(listaPunti[18])
c20=colonna(listaPunti[19])

colonnato=COLOR([1,0.8,0.6])(T([1,2])([10,10])(STRUCT([c,c1,c20,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19])))

altarino=T([1,2])([12.6,9])(COLOR(RED)(SKELETON(1)(CUBOID([1,2,1.5]))))


pirulino = MK([10,10,8])
corona = T([1,2,3])([10,10,4])(MAP(circle(7.6))(INTERVALS(2*PI)(20)))
tetto=COLOR([0.804,0.498,0.196])(JOIN([pirulino,corona]))

VIEW(STRUCT([scalini,cella,colonnato,trabeazione,altarino,SKELETON(1)(tetto)]))

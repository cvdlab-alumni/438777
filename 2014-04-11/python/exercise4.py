from pyplasm import *

def circle(r):
	def circle0(p):
		alpha= p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

def colonna(p):
		x,y=p
		plinto_a=SOLIDIFY(CIRCUMFERENCE(0.5)(80))
		pa=T([1,2])([x,y])(plinto_a)
		pl_a=PROD([pa,Q(0.2)])
		base=STRUCT([T([1,2])([x,y])(CIRCUMFERENCE(0.3)(80))])
		pilastro=PROD([base,Q(10)])
		return COLOR([1,0.8,0.6])(STRUCT([pl_a,pilastro]))


obj = MAP(circle(7.4))(INTERVALS(2*PI)(32))
o=PROD([obj,Q(1.4)])
obj2 = MAP(circle(7.6))(INTERVALS(2*PI)(32))
o2=PROD([obj2,Q(1.2)])
obj3 = MAP(circle(7.8))(INTERVALS(2*PI)(32))
o3=PROD([obj3,Q(1)])
obj4 = MAP(circle(8.0))(INTERVALS(2*PI)(32))
o4=PROD([obj4,Q(0.8)])
obj5 = MAP(circle(8.2))(INTERVALS(2*PI)(32))
o5=PROD([obj5,Q(0.6)])
obj6 = MAP(circle(8.4))(INTERVALS(2*PI)(32))
o6=PROD([obj6,Q(0.4)])
obj7 = MAP(circle(8.6))(INTERVALS(2*PI)(32))
o7=PROD([obj7,Q(0.2)])

scalini=COLOR([0.804,0.498,0.196])(SOLIDIFY((T([1,2])([10,10])(STRUCT([o,o2,o3,o4,o5,o6,o7])))))
#VIEW(T([1,2])(10)(scalini))   //scalini

cella_ax = MAP(circle(4))(INTERVALS(0.9*PI)(32))
c_ax = PROD([cella_ax,Q(10)])
cella_bx = R([1,2])(1.1*PI)(MAP(circle(4))(INTERVALS(0.9*PI)(32)))
c_bx = PROD([cella_bx,Q(10)])
cella_x=STRUCT([c_ax,c_bx])

cella_ay = MAP(circle(3.8))(INTERVALS(0.9*PI)(32))
c_ay = PROD([cella_ay,Q(10)])
cella_by = R([1,2])(1.1*PI)(MAP(circle(3.8))(INTERVALS(0.9*PI)(32)))
c_by = PROD([cella_by,Q(10)])
cella_y=STRUCT([c_ay,c_by])

cella=COLOR([0.698,0,0])(T([1,2,3])([10,10,1.4])(STRUCT([cella_x,cella_y])))
#VIEW(cella)

trab_a = MAP(circle(6))(INTERVALS(2*PI)(32))
trab_ax = PROD([trab_a,Q(0.2)])
trab_b = MAP(circle(6.4))(INTERVALS(2*PI)(32))
trab_bx = PROD([trab_b,Q(0.2)])
trabeazione=COLOR([0.722,0.451,0.2])(SOLIDIFY(T([1,2,3])([10,10,11.4])(STRUCT([trab_ax,trab_bx]))))
#VIEW(trabeazione)

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

colonnato=COLOR([1,0.8,0.6])(T([1,2,3])([10,10,1.4])(STRUCT([c,c1,c20,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19])))
#VIEW(STRUCT([scalini,colonnato,cella,trabeazione]))

altarino=T([1,2,3])([12.6,9,1.4])(COLOR([1,0.141,0])(CUBOID([1,2,1.5])))
#VIEW(STRUCT([scalini,colonnato,cella,trabeazione,altarino]))

pirulino = MK([10,10,14])
corona = T([1,2,3])([10,10,11.6])(MAP(circle(7.6))(INTERVALS(2*PI)(20)))
tetto=COLOR([0.804,0.498,0.196])(JOIN([pirulino,corona]))

tempio=STRUCT([scalini,cella,colonnato,trabeazione,altarino,tetto])

edificio1=COLOR([0.969,0.909,0.624])(T([1,2])([31,1])(CUBOID([10,10,30])))
f11=COLOR([0.12,0.56,1])(T([1,2,3])([32,1,11])(CUBOID([3,0.01,4])))
f12=COLOR([0.12,0.56,1])(T([1,2,3])([37,1,11])(CUBOID([3,0.01,4])))
f13=COLOR([0.12,0.56,1])(T([1,2,3])([32,1,18])(CUBOID([3,0.01,4])))
f14=COLOR([0.12,0.56,1])(T([1,2,3])([37,1,18])(CUBOID([3,0.01,4])))
f15=COLOR([0.12,0.56,1])(T([1,2,3])([32,1,25])(CUBOID([3,0.01,4])))
f16=COLOR([0.12,0.56,1])(T([1,2,3])([37,1,25])(CUBOID([3,0.01,4])))
porta1=COLOR([0.804,0.498,0.196])(T([1,2])([34,1])(CUBOID([4,0.01,8])))
facciata1=STRUCT([f11,f12,f13,f14,f15,f16,porta1])

f21=COLOR([0.12,0.56,1])(T([1,2,3])([31,2,11])(CUBOID([0.01,3,4])))
f22=COLOR([0.12,0.56,1])(T([1,2,3])([31,7,11])(CUBOID([0.01,3,4])))
f23=COLOR([0.12,0.56,1])(T([1,2,3])([31,2,18])(CUBOID([0.01,3,4])))
f24=COLOR([0.12,0.56,1])(T([1,2,3])([31,7,18])(CUBOID([0.01,3,4])))
f25=COLOR([0.12,0.56,1])(T([1,2,3])([31,2,25])(CUBOID([0.01,3,4])))
f26=COLOR([0.12,0.56,1])(T([1,2,3])([31,7,25])(CUBOID([0.01,3,4])))
facciata2=STRUCT([f21,f22,f23,f24,f25,f26])

f31=COLOR([0.12,0.56,1])(T([1,2,3])([32,11,11])(CUBOID([3,0.01,4])))
f32=COLOR([0.12,0.56,1])(T([1,2,3])([37,11,11])(CUBOID([3,0.01,4])))
f33=COLOR([0.12,0.56,1])(T([1,2,3])([32,11,18])(CUBOID([3,0.01,4])))
f34=COLOR([0.12,0.56,1])(T([1,2,3])([37,11,18])(CUBOID([3,0.01,4])))
f35=COLOR([0.12,0.56,1])(T([1,2,3])([32,11,25])(CUBOID([3,0.01,4])))
f36=COLOR([0.12,0.56,1])(T([1,2,3])([37,11,25])(CUBOID([3,0.01,4])))
facciata3=STRUCT([f31,f32,f33,f34,f35,f36])

f41=COLOR([0.12,0.56,1])(T([1,2,3])([41,2,11])(CUBOID([0.01,3,4])))
f42=COLOR([0.12,0.56,1])(T([1,2,3])([41,7,11])(CUBOID([0.01,3,4])))
f43=COLOR([0.12,0.56,1])(T([1,2,3])([41,2,18])(CUBOID([0.01,3,4])))
f44=COLOR([0.12,0.56,1])(T([1,2,3])([41,7,18])(CUBOID([0.01,3,4])))
f45=COLOR([0.12,0.56,1])(T([1,2,3])([41,2,25])(CUBOID([0.01,3,4])))
f46=COLOR([0.12,0.56,1])(T([1,2,3])([41,7,25])(CUBOID([0.01,3,4])))
facciata4=STRUCT([f41,f42,f43,f44,f45,f46])

palazzo1=STRUCT([edificio1,facciata1,facciata2,facciata3,facciata4])
palazzo1=T([1,2])([20,20])(palazzo1)
strada1=COLOR([0.804,0.498,0.196])(T([1,2])([54,10])((CUBOID([4,11,0.05]))))

complesso1=STRUCT([palazzo1,strada1])

edificio2=COLOR([0.969,0.909,0.624])(T([1,2])([88,2])(CUBOID([8,16,40])))

f221=CUBOID([2,0.01,3])
f222=COLOR([0.12,0.56,1])(T([1,2,3])([89,2,11])(STRUCT([f221,T(3)(4)]*7)))
f223=COLOR([0.12,0.56,1])(STRUCT([f222,T(1)(4)]*2))
f224=COLOR([0.12,0.56,1])(STRUCT([f223,T(2)(16)]*2))

porta2=COLOR([0.804,0.498,0.196])(T([1,2])([88,8])(CUBOID([0.01,4,8])))

f225=CUBOID([0.01,2,3])
f226=COLOR([0.12,0.56,1])(T([1,2,3])([88,3,11])(STRUCT([f225,T(2)(4)]*4)))
f227=COLOR([0.12,0.56,1])(STRUCT([f226,T(3)(4)]*7))
f228=COLOR([0.12,0.56,1])(STRUCT([f227,T(1)(8)]*2))

palazzo2=STRUCT([edificio2,f222,f223,f224,f226,f227,f228,porta2])
palazzo2=T(1)(20)(palazzo2)
strada2=COLOR([0.804,0.498,0.196])(T([1,2])([50,8])((CUBOID([58,4,0.05]))))

complesso2=STRUCT([palazzo2,strada2])

edificio3=COLOR([0.969,0.909,0.624])(T([1,2])([104,30])(CUBOID([13,19,47])))

f331=CUBOID([3,0.01,3])
f332=COLOR([0.12,0.56,1])(T([1,2,3])([105,30,11])(STRUCT([f331,T(1)(4)]*3)))
f333=COLOR([0.12,0.56,1])(STRUCT([f332,T(3)(4)]*9))
f334=COLOR([0.12,0.56,1])(STRUCT([f333,T(2)(19)]*2))

porta3=COLOR([0.804,0.498,0.196])(T([1,2])([104,33])(CUBOID([0.01,4,8])))

f335=CUBOID([0.01,3,3])
f336=COLOR([0.12,0.56,1])(T([1,2,3])([104,32,11])(STRUCT([f335,T(2)(4)]*4)))
f337=COLOR([0.12,0.56,1])(STRUCT([f336,T(3)(4)]*9))
f338=COLOR([0.12,0.56,1])(STRUCT([f337,T(1)(13)]*2))
strada3=COLOR([0.804,0.498,0.196])(T([1,2])([50,33])((CUBOID([54,4,0.05]))))

palazzo3=STRUCT([edificio3,f332,f333,f334,porta3,f336,f337,f338])
complesso3=STRUCT([palazzo3,strada3])

palazzo4=T(2)(55)(palazzo2)
strada4=COLOR([0.804,0.498,0.196])(T([1,2])([50,63])((CUBOID([58,4,0.05]))))
complesso4=STRUCT([palazzo4,strada4])

palazzo5=T([1,2])([55,87])(palazzo1)
strada5=COLOR([0.804,0.498,0.196])(T([1,2])([54,67])((CUBOID([4,11,0.05]))))
complesso5=STRUCT([palazzo5,strada5])

palazzo6=T([1,2])([-90,80])(palazzo3)
strada6=COLOR([0.804,0.498,0.196])(T([1,2])([10,95])((CUBOID([4,22,0.05]))))
complesso6=STRUCT([palazzo6,strada6])

palazzo7=T([1,2])([-50,110])(palazzo2)
strada71=COLOR([0.804,0.498,0.196])(T([1,2])([45,95])((CUBOID([4,27,0.05]))))
strada72=COLOR([0.804,0.498,0.196])(T([1,2])([49,118])((CUBOID([10,4,0.05]))))
complesso7=STRUCT([palazzo7,strada71,strada72])

palazzo8=T(2)(55)(palazzo1)
strada81=COLOR([0.804,0.498,0.196])(T([1,2])([0,95])((CUBOID([112,4,0.05]))))
strada82=COLOR([0.804,0.498,0.196])(T([1,2])([109,95])((CUBOID([4,20,0.05]))))
complesso8=STRUCT([palazzo8,strada81,strada82])

base1=COLOR([0.09,0.45,0.27])(T(1)(50)((CUBOID([70,132]))))
base2=COLOR([0.09,0.45,0.27])(T(2)(95)((CUBOID([120,38]))))
base=STRUCT([base1,base2])
stradone=COLOR([0.804,0.498,0.196])(T(1)(84)((CUBOID([6,133,0.05]))))
prato=COLOR([0.011,0.753,0.235])(CUBOID([50,95]))

complesso=STRUCT([(T([1,2])([5,10])(tempio)),complesso1,complesso2,complesso3,complesso4,complesso5,complesso6,complesso7,complesso8,prato,base,stradone])
#VIEW(complesso)

tronco=COLOR([0.588,0.294,0])(CYLINDER([0.25,7])(40))
chioma=COLOR([0.133,0.545,0.133,100])(T(3)(7)((SPHERE(1.5)([20,20]))))
albero=STRUCT([tronco,chioma])

a1=T([1,2])([48,2])(albero)
a2=(STRUCT([a1,T(2)(3)]*2))
a3=T([1,2])([48,14])(albero)
a4=(STRUCT([a3,T(2)(3)]*7))
a5=T([1,2])([48,40])(albero)
a6=(STRUCT([a5,T(2)(3)]*8))
a7=T([1,2])([48,70])(albero)
a8=(STRUCT([a7,T(2)(3)]*7))

a9=T([1,2])([2,94])(albero)
a10=(STRUCT([a9,T(1)(3)]*3))
a11=T([1,2])([16,94])(albero)
a12=(STRUCT([a11,T(1)(3)]*10))

a13=(STRUCT([albero,T(2)(3)]*32))
a14=(STRUCT([albero,T(1)(3)]*17))

alberi=STRUCT([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14])

albero2=S([1,2,3])([1,1,2])(albero)

a21=T(1)(52)(albero2)
a22=(STRUCT([a21,T(1)(3)]*11))

a23=T(1)(119)(albero2)
a24=(STRUCT([a23,T(2)(3)]*44))
a28=(STRUCT([a23,T(1)(-3)]*10))

a25=T([1,2])([1,131])(albero2)
a26=(STRUCT([a25,T(1)(3)]*28))
a27=(STRUCT([a25,T(2)(-3)]*11))

a29=T([1,2])([119,131])(albero2)
a30=(STRUCT([a29,T(1)(-3)]*10))

alberiTotali=STRUCT([a21,a22,alberi,a23,a24,a25,a26,a27,a28,a29,a30])
#VIEW(STRUCT([complesso,alberiTotali]))

pilastro=COLOR(BLACK)(CYLINDER([0.2,1.5])(40))
plinto=COLOR(BLACK)(T(3)(1.5)((CYLINDER([0.5,0.5])(40))))
luce=COLOR([1,0.937,0.835])(T(3)(2)((SPHERE(0.5)([20,20]))))
lampioncino=STRUCT([pilastro,plinto,luce])

l1=T([1,2])([52,8])(lampioncino)
l2=(STRUCT([l1,T(1)(10)]*6))
l3=(STRUCT([l2,T(2)(4)]*2))
l4=(STRUCT([l2,T(2)(25)]*2))
l5=(STRUCT([l4,T(2)(4)]*2))
l6=(STRUCT([l2,T(2)(55)]*2))
l7=(STRUCT([l6,T(2)(4)]*2))
l8=(STRUCT([l2,T(2)(87)]*2))

pilastro=COLOR(BLACK)(CYLINDER([0.2,8])(40))
plinto=COLOR(BLACK)(T(3)(8)((CYLINDER([0.5,0.5])(40))))
luce=COLOR([1,0.937,0.835])(T(3)(8.5)((SPHERE(0.5)([20,20]))))
lampione=STRUCT([pilastro,plinto,luce])
la1=T([1,2])([84,1])(lampione)
la2=(STRUCT([la1,T(2)(14.5)]*10))
la3=(STRUCT([la2,T(1)(6)]*2))

l9=T([1,2])([22,99])(lampioncino)
l10=(STRUCT([l9,T(1)(10)]*9))

l11=T([1,2])([10,102])(lampioncino)
l12=(STRUCT([l11,T(2)(4)]*2))
l13=(STRUCT([l12,T(1)(4)]*2))
l14=(STRUCT([l13,T(1)(99)]*2))

l15=T([1,2])([49,102])(lampioncino)
l16=(STRUCT([l15,T(2)(4)]*6))
l17=(STRUCT([l16,T(1)(-4)]*2))

luci=STRUCT([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,la1,la2,la3])
#VIEW(STRUCT([complesso,alberiTotali,luci]))

gamba1=CUBOID([0.25,0.5,1])
gamba2=T(1)(2.75)(gamba1)
gamba3=T(2)(1.5)(gamba1)
gamba4=T(1)(2.75)(gamba3)
seduta=T(3)(1)(CUBOID([3,1.5,0.25]))
schienale=T([2,3])([1.5,1])((CUBOID([3,0.5,1.5])))
panchina=COLOR([0.5765,0.5765,0.5765])(STRUCT([gamba1,gamba2,gamba3,gamba4,seduta,schienale]))

p1=T([1,2])([18,91])(panchina)
p2=(STRUCT([p1,T(1)(4)]*4))

p3=T([1,2])([46,58])((R([1,2])(-PI/2)(panchina)))
p4=(STRUCT([p3,T(2)(-4)]*4))

p5=T([1,2])([46,88])((R([1,2])(-PI/2)(panchina)))
p6=(STRUCT([p5,T(2)(-4)]*4))

p7=T([1,2])([46,30])((R([1,2])(-PI/2)(panchina)))
p8=(STRUCT([p7,T(2)(-4)]*4))

p9=T([1,2])([5,2])((R([1,2])(-PI)(panchina)))
p10=(STRUCT([p9,T(1)(5.5)]*8))

p11=T([1,2])([2.5,4])((R([1,2])(PI/2)(panchina)))
p12=(STRUCT([p11,T(2)(5.5)]*17))

panchine=STRUCT([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12])

#VIEW(STRUCT([complesso,alberiTotali,luci,panchine]))

stelo=COLOR([0.011,0.753,0.235])(CYLINDER([0.05,1])(40))
corolla=CIRCUMFERENCE(0.25)(80)
puntoCorolla=MK([0,0,0.35])
petali=COLOR(RED)(JOIN([corolla,puntoCorolla]))
fiore=T([1,2,3])([0,0,1])(R([1,3])(PI)(STRUCT([stelo,petali])))
f1=S([1,2,3])([0.5,0.5,1])(fiore)
#VIEW(f1)

baseInferioreVaso=CIRCUMFERENCE(3)(80)
baseSuperioreVaso=T(3)(3)(JOIN((CIRCUMFERENCE(5)(80))))
terra= COLOR([0.396,0.263,0.129])(T(3)(3.1)(JOIN(CIRCUMFERENCE(4)(80))))
contenitore=COLOR([0.804,0.498,0.196])(JOIN([baseSuperioreVaso,baseInferioreVaso]))
vaso=STRUCT([contenitore,terra])
f2=T([1,2,3])([-2.4,-2.4,3])(f1)
f3=(STRUCT([f2,T(1)(0.3)]*18))
f4=(STRUCT([f3,T(2)(0.3)]*18))
vasoConFiori=STRUCT([vaso,f2,f3,f4])
v1=T([1,2])([25,40])(vasoConFiori)
v2=T([1,2])([25,55])(vasoConFiori)
v3=T([1,2])([25,70])(vasoConFiori)
v4=T([1,2])([35,105])(vasoConFiori)
v5=T(1)(40)(v4)
v6=(STRUCT([v5,T(2)(-27)]*4))
v7=(STRUCT([v6,T(1)(24)]*2))
vasi=STRUCT([v1,v2,v3,v4,v5,v6,v7])

VIEW(STRUCT([complesso,alberiTotali,luci,panchine,vasi]))


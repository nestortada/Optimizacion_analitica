Sets

i tipo de quimico i1=A i2=S1A i3= S2A  /i1*i3/
;

Variable
z función objetivo
;

Positive Variable
x(i)
;

Equation
R1 Almacenamiento
R2 Empacque químico A
R3 Capacidad de Producción
R4 Capacidad de Producción
R5 Capacidad de Producción
R6 Tres partes 
FO Función Objetivo
;

R1..(x("i1"))+ (x("i2"))+(x("i3"))=L= 100000;
R2..(x("i1"))=G= 60000;
R3..(x("i3"))=L=12000;
R4..(x("i1"))+ (x("i2"))+(x("i3"))=L= 80000;
R5..(x("i2"))=L= 40000;
R6..3*(x("i2"))=E= (x("i3"));
FO..z=E= 200*(x("i1"))+300*(x("i2"))+320*(x("i3"));

model punto3 /all/;

solve punto3 using lp maximizing z
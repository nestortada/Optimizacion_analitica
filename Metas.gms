Sets
i tipo de silla /i1*i3/;

Parameter
MA(i) Kg de madera /i1 8, i2 6, i3 14/
HF(i) Horas de fabricación /i1 4, i2 8, i3 6/
HA(i) kjsa /i1 4, i2 6, i3 8/
PV(i) Precio de venta por cada silla de tipo i /i1 140, i2 220, i3 220/;

Variables
*Z Fo
P1 prioridad 1- responde a la meta 1
P2 prioridad 1- responde a la meta 2
P3 prioridad 1- responde a la meta 3
Positive Variable
dn1, dp1, dn2, dp2 , dn3, dp3, dn4,dp4,dn5,dp5;
Integer Variable
x(i) # De sillas i;

Equation
*FO
meta1, meta2, meta3, M1, M2, M3,M4,M5, R1, R2, R3;

*FO.. z =E= sum(i, x(i) * PV(i));
meta1.. P1 =E= dn1 + dp1;
meta2.. P2 =E= dn2 + dp2;
meta3.. P3=E= dn3 +dn4 + dn5;
M1.. sum(i, x(i) * PV(i)) + dn1 - dp1 =E= 360000;   
M2.. sum(i, x(i) * MA(i))+dn2 -dp2  =E= 18000;
M3..x('i1')*PV('i1')+dn3-dp3 =E= 140000;
M4..x('i2')*PV('i2')+dn4-dp4 =E= 120000;
M5..x('i2')*PV('i2')+dn5-dp5 =E= 75000;

R1.. sum(i, x(i) * MA(i)) =L= 18000;
R2.. sum(i, x(i) * HF(i)) =L= 12000;
R3.. sum(i, x(i) * HA(i)) =L= 10400;

model paso1 /M1, R1, R2, R3, meta1/;
solve paso1 using MIP minimizing P1

Equation
l_meta1;
l_meta1.. dn1 + dp1 =E= P1.l;

model paso2 /M1, M2, meta2, R2, R3, l_meta1/;
solve paso2 using MIP minimizing P2

Equation
l_meta2;
l_meta2..dn2+dp2 =E=P2.l

model paso3 /M1,M2,M3,M4,M5,meta3,R2,R3,l_meta1,l_meta2/;
solve paso3 using MIP minimizing P3

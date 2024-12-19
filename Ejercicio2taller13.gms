Sets
i lotes del producto i a producir i1= pasteles i2= galletas /i1*i2/
;

Variable
z función objetivo
;

Positive Variable
x(i)
;

Equation
R1 Horas de preparación
R2 Horas de horneado
FO Función Objetivo
;

R1..4*(x("i1"))+3*(x("i2"))=L= 40;
R2..4*(x("i1"))+7*(x("i2"))=L= 56;
FO..z=E= 70*(x("i1"))+90*(x("i2"));

model punto2 /all/;

solve punto2 using lp maximizing z

$onText
El marginal arroja un valor de 9.375, por lo cual el aumento de 16 horas daría un aumento en las
ganancias de 150, aunque las horas de preparación son un limitante, al aumenar las horas de
horneado la organización de cantidad de producto a producir cambia, por lo cual al final
este aumento de horas si genera una ganancia a la panadería
$offText

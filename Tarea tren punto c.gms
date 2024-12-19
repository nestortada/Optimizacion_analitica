$onText
Ejercicio 2 punto C
$offText

Set
i origen /i1*i3/
j mercados /j1*j5/
;

Parameter
Capacidad_i (i) /i1 15, i2 20, i3 15/
Demanda_j (j) /j1 11, j2 12, j3 9 , j4 10, j5 8/
;

table cost_i_j (i,j)
        j1  j2  j3  j4  j5
     i1 61  72  45  55  66
     i2 69  78  60  49  56
     i3 59  66  63  61  47
;

table costo_barco_i_j (i,j)
        j1   j2   j3   j4   j5
     i1 31   38   24   1E10 35
     i2 36   43   28   24   31
     i3 1E10 33   36   32   26
;

table inversion_i_j (i,j)
        j1   j2   j3   j4   j5
     i1 275  303  238  1E10 285
     i2 293  318  270  250  265
     i3 1E10 283  275  268  240
;

Variable
z3 FO
;

Positive Variable
x(i,j) Millones de pies lineales de madera transpaotados desde el origen i hasta el mercado j por tren
y(i,j) Millones de pies lineales de madera transpaotados desde el origen i hasta el mercado j por barco

Equation
R1 capacidad
R2 Demadna
FO
;

R1(i)..sum(j,x(i,j)+y(i,j))=L=Capacidad_i(i);
R2(j)..sum(i,x(i,j)+y(i,j))=G=Demanda_j(j);
FO..z3=E=sum((i,j), x(i,j)*cost_i_j(i,j)+y(i,j)*costo_barco_i_j(i,j) + 0.1*y(i,j)*inversion_i_j(i,j))

model transb /all/;
solve transb using lp minimizing z3

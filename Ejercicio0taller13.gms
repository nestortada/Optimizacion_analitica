Sets
i tipo de producto i1 = tablero I2 = Cajas /i1,i2/
;
Variable
z Función objetico
;

Positive Variable
x(i)
;

Equation
R1 Capacidad de almacen
R2 Permitido de contamicación
FO Función Objetivo
;

R1..20*(x("i1"))+10*(x("i2"))=L= 2000;
R2.. 0.02*(x("i1")) +0.03*(x("i2")) =L= 1;
FO..z=E= 100000*(x("i1")) + 50000*(x("i2"));

model Punto0 /all/;
solve Punto0 using lp maximizing z


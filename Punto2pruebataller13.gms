Sets
i mg de compuesto /i1*i4/
j tipo de medicamento /j1*j2/
k tipo de frabrica /k1*k2/
l tipo de CD /l1*l4/
;

Parameter
precio_i(i) /i1 0 ,i2 350,i3 800,i4 550/
disponibilidad_i(i) /i1 1E200, i2 10000000, i3 8000000,i4 12000000/
demanda1_l(l) / l1 120000, l2 145000, l3 80000, l4  35000/
demanda2_l (l) / l1 6500, l2 12300,  l3 2600, l4  800/
preciofab_j(j) /j1 2300, j2 2600/

;
Table transporte_k_l (k,l)       
        l1          l2          l3          l4
    k1  4.5E-6      0.015E-6    0.8E-6      15E-6
    k2  65E-6       3.5E-6      3.8E-6      0.34E-6
;

    

Variable
w Función objetivo
;

Positive Variable

x(i,j,k) # mg de compuesto i para fabricar medicamento j en la fábrica k
y(j,k) # mg de medicamento j elaborados en la fabrica k
z(j,k,l) # mg de medicamento j elaborados en la fabrica k en el CD l 
;




Equation
R1 disponibilidad
R2 demanda1
R3 demadna2
R4 porcentaje menor x11
R5 procentaje menor x21
R6 procentaje menor x31
R7 Función de equilibrio 1
R8 procentaje menor x12
R9 procentaje menor x22
R10 procentaje menor x32
R11 procentaje menor x42
R12 Función de equilibrio 2
FO Función objetivo
;
R1(i).. sum((j,k),x(i,j,k))=L=disponibilidad_i(i);
R2(l).. sum(k, z("j1",k,l))=G= demanda1_l(l)*5;
R3(l).. sum(k ,z("j2",k,l))=G= demanda2_l(l)*8;
R4(k).. x("i1","j1", k) =L= 0.35*sum(i, x(i, "j1",k));
R5(k).. x("i2","j1",k) =L= 0.15*sum(i, x(i, "j1",k));
R6(k).. x("i3","j1",k) =L= 0.10*sum(i, x(i, "j1",k));
R7(j).. sum((i,k), x(i,j,k)) =E= sum((k), y(j,k) );
R8(k).. x("i1","j2",k) =E= 0.40*sum(i, x(i, "j2",k));
R9(k).. x("i2","j2",k) =E= 0.15*sum(i, x(i, "j2",k));
R10(k).. x("i3","j2",k) =E= 0.10*sum(i, x(i, "j2",k));
R11(k).. x("i4","j2",k) =E= 0.35*sum(i, x(i, "j2",k));
R12(j).. sum(k,y(j,k)) =E= sum((k,l), z(j,k,l));


Fo..w=E= sum((i,j,k), x(i,j,k)*precio_i(i)) + sum((j,k), y(j,k)* preciofab_j(j)) +  sum((j,k,l) , z(j,k,l)*transporte_k_l (k,l))

model Punto2 /all/;
solve Punto2 using lp minimazing w

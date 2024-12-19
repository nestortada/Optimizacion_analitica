$onText
Sets

i Fábricas /i1,i2/
j Bodegas /j1,j2/
k Cds /k1,k2/
l Clientes /l1*l3/
;

Parameters

oferta_i(i) /i1 100, i2 100/
capacidad_b(j) /j1 80, j2 100/
capacidad_cd(k) /k1 100, k2 100/
dem(l) /l1 40, l2 80, l3 80/
;

table costo_i_j (i,j)

        j1  j2
    i1  40  30  
    i2  40  50
;

table costo_j_k(j,k)

        k1  k2
    j1  50  70
    j2  80  60
;

table costo_k_l (k,l)

        l1  l2  l3
    k1  60  40  0
    k2  0   20  90
;

table costo_i_l (i,l)

        l1  l2  l3
    i1  140 0   0
    i2  0   0   150
   
;

Variable
FO1 FO
;

Positive Variable
x(i,j) Producto enviado desde la fábrica i hasta la bodega j
y(j,k) Producto enviado desde la bodega j hasta el CD k
z(k,l) Producto enviado desde el CDk hasta el cliente l
w(i,l) Producto enviado desde la fábrica i hasta el cliente l
c23 Producto enviado desde el cliente 2 al cliente 3
;

Equation

R1 oferta de las fábricas
R2 Capacidad de las bodegas
R3 Capacidad de los Cds
R4 Demanda cliente 1
R5 Demanda cliente 2
R6 Deamnda cliente 3
R7 Equilibrio bodegas
R8 Equilibio Cds
R9 Restricción de envío
R10
R11
R12
R13
R14
FO
;

R1(i)..sum(j,x(i,j)) =L= oferta_i(i);
R2(j)..sum(i,x(i,j)) =L= capacidad_b(j);
R3(k)..sum(j,y(j,k)) =L= capacidad_cd(k);
R4(l)..sum(k,z(k,l))+sum(i,w(i,l))=G= dem("l1");
R5(l)..sum(k,z(k,l))+sum(i,w(i,l))=G= dem("l2")+c23;
R6(l)..sum(k,z(k,l))+sum(i,w(i,l))+c23=G= dem("l3");
R7(j)..sum(i,x(i,j)) =E= sum(k,y(j,k));
R8(k)..sum(j,y(j,k)) =E= sum(l,z(k,l));
R9..z("k2","l1")=E=0;
R10..z("k1","l3")=E=0;
R11..w("i2","l1")=E=0;
R12.. w("i1","l2")=E=0;
R13..w("i1","l3")=E=0;
R14..w("i2","l2")=E=0;
FO..FO1 =E= sum((i,j),x(i,j)*costo_i_j (i,j))+sum((j,k),y(j,k)*costo_j_k(j,k))+sum((k,l),z(k,l)*costo_k_l (k,l))+sum((i,l),w(i,l)*costo_i_l (i,l))+(20*c23);

model transb /all/;
solve transb using lp minimizing FO1
$offText

Sets

i Fábricas /i1,i2/
j Bodegas /j1,j2/
k Cds /k1,k2/
l Clientes /l1*l3/
;

Parameters

oferta_i(i) /i1 100, i2 100/
capacidad_b(j) /j1 80, j2 100/
capacidad_cd(k) /k1 100, k2 100/
dem(l) /l1 40, l2 80, l3 80/
;

table costo_i_j (i,j)

        j1  j2
    i1  40  30  
    i2  40  50
;

table costo_j_k(j,k)

        k1  k2
    j1  50  70
    j2  80  60
;

table costo_k_l (k,l)

        l1      l2  l3
    k1  60      40  1E10
    k2  1E10    20  90
;

table costo_i_l (i,l)

        l1      l2          l3
    i1  140     1E10        1E10
    i2  1E10    1E10        150
   
;

Variable
FO1 FO
;

Positive Variable
x(i,j) Producto enviado desde la fábrica i hasta la bodega j
y(j,k) Producto enviado desde la bodega j hasta el CD k
z(k,l) Producto enviado desde el CDk hasta el cliente l
w(i,l) Producto enviado desde la fábrica i hasta el cliente l
c23 Producto enviado desde el cliente 2 al cliente 3
;

Equation

R1 oferta de las fábricas
R2 Capacidad de las bodegas
R3 Capacidad de los Cds
R4 Demanda cliente 1
R5 Demanda cliente 2
R6 Deamnda cliente 3
R7 Equilibrio bodegas
R8 Equilibio Cds
FO
;

R1(i)..sum(j,x(i,j)) =L= oferta_i(i);
R2(j)..sum(i,x(i,j)) =L= capacidad_b(j);
R3(k)..sum(j,y(j,k)) =L= capacidad_cd(k);
R4(l)..sum(k,z(k,l))+sum(i,w(i,l))=G= dem("l1");
R5(l)..sum(k,z(k,l))+sum(i,w(i,l))=G= dem("l2")+c23;
R6(l)..sum(k,z(k,l))+sum(i,w(i,l))+c23=G= dem("l3");
R7(j)..sum(i,x(i,j)) =E= sum(k,y(j,k));
R8(k)..sum(j,y(j,k)) =E= sum(l,z(k,l));
FO..FO1 =E= sum((i,j),x(i,j)*costo_i_j (i,j))+sum((j,k),y(j,k)*costo_j_k(j,k))+sum((k,l),z(k,l)*costo_k_l (k,l))+sum((i,l),w(i,l)*costo_i_l (i,l))+(20*c23);

model transb /all/;
solve transb using lp minimizing FO1
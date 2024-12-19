$onText
Sets
i Refinería de tipo i /i1*i3/
j CD j /j1*j4/
;
Variable
z FO
;
positive Variable
x(i,j) # de barriles vendidos de la refinería i al CDj
y(i) # de barriles añadidos a la capacidad de la refinería j
;
Equation
R1 capacidad de la refinería i
R2
R3
R4 Demanda
R5
R6
R7
R8
R9
R10
R11
* Presupuesto maximo
R12
* Por lo menos 25% del preuspuesto
R13
R14
R15
FO
;
*va iterando en j para todo i
R1..x("i1","j1")+x("i1","j2")+x("i1","j3")+x("i1","j4")=L=2500+y("i1"); 
R2..x("i2","j1")+x("i2","j2")+x("i2","j3")+x("i2","j4")=L=3000+y("i2");
R3..x("i3","j1")+x("i3","j2")+x("i3","j3")+x("i3","j4")=L=4000+y("i3");

R4..x("i1","j1")+x("i2","j1")+x("i3","j1")=L=4000;
R5..x("i1","j2")+x("i2","j2")+x("i3","j2")=L=5000;
R6..x("i1","j3")+x("i2","j3")+x("i3","j3")=L=6000;
R7..x("i1","j4")+x("i2","j4")+x("i3","j4")=L=9000;

R8..x("i1","j1")+x("i2","j1")+x("i3","j1")=G=0.8*4000;
R9..x("i1","j2")+x("i2","j2")+x("i3","j2")=G=0.8*5000;
R10..x("i1","j3")+x("i2","j3")+x("i3","j3")=G=0.8*6000;
R11..x("i1","j4")+x("i2","j4")+x("i3","j4")=G=0.8*9000;

*Presupuesto Máximo
R12..0.125*y("i1")+0.14*y("i2")+0.17*y("i3")=L=1500;


R13..x("i1","j1")+x("i1","j2")+x("i1","j3")+x("i1","j4")=G=0.25*(x("i1","j1")+x("i1","j2")+x("i1","j3")+x("i1","j4")+x("i2","j1")+x("i2","j2")+x("i2","j3")+x("i2","j4")+x("i3","j1")
+x("i3","j2")+x("i3","j3")+x("i3","j4"));
R14..x("i2","j1")+x("i2","j2")+x("i2","j3")+x("i2","j4")=G=0.25*(x("i1","j1")+x("i1","j2")+x("i1","j3")+x("i1","j4")+x("i2","j1")+x("i2","j2")+x("i2","j3")+x("i2","j4")+x("i3","j1")
+x("i3","j2")+x("i3","j3")+x("i3","j4"));
R15..x("i3","j1")+x("i3","j2")+x("i3","j3")+x("i3","j4")=G=0.25*(x("i1","j1")+x("i1","j2")+x("i1","j3")+x("i1","j4")+x("i2","j1")+x("i2","j2")+x("i2","j3")+x("i2","j4")+x("i3","j1")
+x("i3","j2")+x("i3","j3")+x("i3","j4"));
FO.. z=E= 1.6*x("i1","j1")+2*x("i1","j2")+1.2*x("i1","j3")+1.3*x("i1","j4")+1.2*x("i2","j1")+
1.6*x("i2","j2")+1.5*x("i2","j3")+1.8*x("i2","j4")+2.5*x("i3","j1")
+1.8*x("i3","j2")+1.65*x("i3","j3")+x("i3","j4")-(0.125*y("i1")+0.14*y("i2")+0.17*y("i3"));
model sol_p2 /all/;
solve sol_p2 using LP maximizing z
$offText


Sets

i refineria de tipo i /i1*i3/
j centro de distribución j /j1*j4/
;

Parameter
dem_max(j) Demanda maxima de los CDs j /j1 4000, j2 5000, j3 6000, j4 9000/
cap_ref(i) Capacidad de la refineria i /i1 2500, i2 3000, i3 4000/
costo_cap_add_(i) capacidad añadida en barriles para la refineria i /i1 0.125, i2 0.14, i3 0.17/
;

* Matriz de beneficio enviar barriles desde la refineria i hasta el CDs j

Table matriz_beneficios(i,j)

        j1      j2      j3      j4
    i1  1.6     2       1.2     1.3
    i2  1.2     1.6     1.5     1.8 
    i3  2.5     1.8     1.65    1
;

Variable
z función objetivo
;

Positive Variable
x(i,j) Numero de barriles enviados desde la refineria i hasta el centro de distrivución j
y(i) barriles añadidos a la capacidad de la refineria i
pt Producción final
;

Equation
R1 Capacidad de la refineria i
R2 demanda minima
R3 Demanda maxima
R4 Presupuesto para añadir barriles a la capacidad de la refineria
R5 25% de la producción final
R6 Ecuación de producción total
FO Función objetivo
;

R1(i)..sum(j,x(i,j))=L=cap_ref(i)+y(i);
R2(j)..sum(i,x(i,j))=G=dem_max(j)*0.8;
R3(j)..sum(i,x(i,j))=L=dem_max(j);
R4..sum(i,y(i)*costo_cap_add_(i))=L=1500;
R5(i)..sum(j,x(i,j))=G= 0.25*pt;
R6..pt=E=sum((i,j), x(i,j));
FO..z=E=sum((i,j),x(i,j)*matriz_beneficios(i,j))-sum(i,y(i)*costo_cap_add_(i));

model sol_p2 /all/;
solve sol_p2 using LP maximizing z



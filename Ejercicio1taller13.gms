Sets

i tipo de horas i1=A i2= B /i1*i2/
;

Variable
z función objetivo
;

Positive Variable
x(i)
;

Equation
R1 Capacidad de horas hombre
R2 Capacidad de hombres máquina
R3 Demanda
FO Función Objetivo
;

R1..30*(x("i1"))+20*(x("i2"))=L= 2700;
R2..5*(x("i1"))+10*(x("i2"))=L= 850;
R3..(x("i1"))+(x("i2"))=G= 95;
FO..z=E= 20*(x("i1"))+40*(x("i2"));

model punto1 /all/;

solve punto1 using lp maximazing z

$onText
La inversión de la empresa es incrorecta porque no maximiza los beneficios
de la empresa pues las horas de ingeniero no dan mayor utilidad mientras
que las de máquina si. Cada hora de máquina más da $4 más, en cambio las
horas ingenieron no aumentan beneficio.
$offText

$onText
La empresa podría reducir su acuerdo con el cliente porque no perdería dinero
pero no es que los beneficios vayan a aumentar, se van a mantener.
$offText
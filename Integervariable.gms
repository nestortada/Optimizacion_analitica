Sets
    i tipo_de_prenda /i1*i3/;

Parameters
    mano_obra_i(i) /i1 3, i2 2, i3 6/
    tela_i(i) /i1 4, i2 3, i3 4/
    precio_venta_i(i) /i1 12, i2 8, i3 15/
    costo_i(i) /i1 6, i2 4, i3 8/
    alquiler_i(i) /i1 200, i2 150, i3 100/;

Variables
    z;

Binary Variables
    b(i); 

Integer Variables
    x(i);  

Equations
    R1, R2, R3, FO;

R1.. sum(i, x(i) * mano_obra_i(i)) =L= 150;
R2.. sum(i, x(i) * tela_i(i)) =L= 160;
R3(i).. x(i) =L= b(i)* 1E15;
FO.. z =E= sum(i, x(i) * precio_venta_i(i)) - sum(i, x(i) * costo_i(i)) - sum(i, alquiler_i(i)*b(i));

Model ropa /all/;
Solve ropa using mip maximizing z;


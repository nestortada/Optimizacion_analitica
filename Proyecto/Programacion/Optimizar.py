import subprocess
import sys


import sys
import subprocess

# Lista de módulos que necesitas verificar e instalar
modules = [
    "importlib", "tkinter", "pandas", "os", "matplotlib", 
    "openpyxl", "sqlite3", "pulp", "plotly", "numpy", "kaleido"
]

def check_and_install(module):
    try:
        __import__(module)
        print(f"{module} ya está instalado.")
    except ImportError:
        print(f"Instalando {module}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        print(f"{module} instalado exitosamente.")


for module in modules:
    check_and_install(module)



from pulp import *
import importlib
import Base_Datoss as bd
import triggers as t
import Vistas as v
importlib.reload(bd)
importlib.reload(t)
importlib.reload(v)
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox, filedialog, Label
from tkinter.ttk import Progressbar
import pandas as pd
import os
import matplotlib.pyplot as plt
import subprocess
import traceback
from tkinter.filedialog import askopenfilename
from collections import defaultdict
import numpy as np
from collections import defaultdict
import os


def log_error_to_file(error_message):
    
    root = Tk()
    root.withdraw()

    
    folder_path = filedialog.askdirectory(title="Selecciona una carpeta para guardar el archivo de errores")
    
    if folder_path:
        error_log_path = os.path.join(folder_path, "error_log.txt")  
        with open(error_log_path, "a") as error_file:
            error_file.write(error_message + "\n\n")

        
        subprocess.Popen(['notepad.exe', error_log_path])  
        print(f"Error guardado en: {error_log_path}")
    else:
        print("No se seleccionó ninguna carpeta para guardar el error.")




try:
    root = Tk()
    root.withdraw()
    

    progress_window = Tk()
    progress_window.title("Progreso")
    progress_window.geometry("400x100")

    progress_label = Label(progress_window, text="Progreso del proceso")
    progress_label.pack(pady=10)

    progress_bar = Progressbar(progress_window, length=300, mode='determinate')
    progress_bar.pack(pady=10)

    total_steps = 100
    current_step = 0

    
    
    messagebox.showinfo("Información", "Por favor, seleccione el archivo de Excel.")
    path = askopenfilename(defaultextension=".xlsm", 
                           filetypes=[("Excel files", "*.xlsm;*.xlsx;*.xls")],
                           title="Selecciona el archivo de Excel con macros")

    if not path:
        messagebox.showerror("Error", "No se seleccionó ningún archivo. El programa se cerrará.")
        sys.exit()

    
    messagebox.showinfo("Información", "Por favor, crea o selecciona una base de datos.")
    db_path = asksaveasfilename(defaultextension=".db", 
                                filetypes=[("SQLite DB files", "*.db")],
                                title="Selecciona o crea la base de datos")
    
    if not db_path:
        messagebox.showerror("Error", "No se seleccionó ningún archivo. El programa se cerrará.")
        sys.exit()

    

    
    excel_directory = os.path.dirname(path)
    design_directory = os.path.join(excel_directory, "Diseño")

    
    if not os.path.exists(design_directory):
        os.makedirs(design_directory)

    
    directory = design_directory


    current_step = bd.create_allDB(path=path, db_path=db_path, progress_bar=progress_bar, 
                                   progress_window=progress_window, total_steps=total_steps, current_step=current_step)
    current_step = t.create_allTD(conectar=db_path, current_step=current_step, total_steps=total_steps, 
                                  progress_bar=progress_bar, progress_window=progress_window)
    current_step = v.create_allV(conectar=db_path, current_step=current_step, total_steps=total_steps, 
                                 progress_bar=progress_bar, progress_window=progress_window, directory=directory)

    df_CL_C = pd.read_csv(os.path.join(directory, 'df_CL_C.csv'))
    df_CL_C_F = pd.read_csv(os.path.join(directory, 'df_CL_C_F.csv'))
    df_CL_C_V = pd.read_csv(os.path.join(directory, 'df_CL_C_V.csv'))
    df_CC_C = pd.read_csv(os.path.join(directory, 'df_CC_C.csv'))
    df_CC_C_F = pd.read_csv(os.path.join(directory, 'df_CC_C_F.csv'))
    df_CC_C_V = pd.read_csv(os.path.join(directory, 'df_CC_C_V.csv'))
    df_D = pd.read_csv(os.path.join(directory, 'df_D.csv'))
    df_Flete_P = pd.read_csv(os.path.join(directory, "df_Flete_P.csv"))
    df_Flete_S = pd.read_csv(os.path.join(directory, "df_Flete_S.csv"))
    df_materiales = pd.read_csv(os.path.join(directory, 'df_materiales.csv'))

    o = df_materiales["Tipo_Almacenamiento"].unique().tolist() # diccionario  para tipo de almacenamiento

    productos = {} 


    for i in o:
        productos[f'{i}'] = df_materiales[df_materiales["Tipo_Almacenamiento"] == i]["Agrupaciones"].tolist()

    df_planta_C = {} #filtrado de las tsablas de costos iniciales por agrupaciones que son el tipo de almacenameinto
    for i in o:
        df_filtrado = df_CL_C[df_CL_C['Agrupaciones'].isin(productos[i])]
        df_filtrado.index = df_filtrado['Agrupaciones']
        df_filtrado = df_filtrado.drop(columns=['Agrupaciones'])
        df_planta_C[f'{i}'] = df_filtrado

    
    df_planta_CF= {}

    for i in o:
        df_filtrado = df_CL_C_F[df_CL_C_F['Agrupaciones'].isin(productos[i])]
        df_filtrado.index = df_filtrado['Agrupaciones']
        df_filtrado = df_filtrado.drop(columns=['Agrupaciones'])
        df_planta_CF[f'{i}'] = df_filtrado

    df_CL_C_V.iloc[:, 1:] = df_CL_C_V.iloc[:, 1:].replace(0, 1E9)
    df_planta_CV= {}

    for i in o:
        df_filtrado = df_CL_C_V[df_CL_C_V['Agrupaciones'].isin(productos[i])]
        df_filtrado.index = df_filtrado['Agrupaciones']
        df_filtrado = df_filtrado.drop(columns=['Agrupaciones'])
        df_planta_CV[f'{i}'] = df_filtrado

    df_flete_CV= {}

    for i in o:
        if not isinstance(i, list):
            e = [i]
        df_Flete_P["Origen"] = df_Flete_P["Origen"].astype(str).str.strip()
        df_filtrado = df_Flete_P[df_Flete_P["Tipo_Transporte"].isin(e) & (df_Flete_P["Origen"] != "FUNZA")].drop(columns=['ID','Tipo_Transporte', 'Eliminar'])
        pivot_df = df_filtrado.pivot(index='Origen', columns='Destino', values='Flete')
        pivot_df = pivot_df.fillna(1E18)
        df_flete_CV[f'{i}'] = pivot_df

    df_Funza = {}
    for i in o:
        if not isinstance(i, list):
            e = [i]
        df_Flete_P["Origen"] = df_Flete_P["Origen"].astype(str).str.strip()
        df_filtrado = df_Flete_P[df_Flete_P["Tipo_Transporte"].isin(e) & (df_Flete_P["Origen"] == "FUNZA")].drop(columns=['ID', 'Tipo_Transporte', 'Eliminar'])
        

        pivot_df = df_filtrado.pivot(index='Origen', columns='Destino', values='Flete')
        pivot_df = pivot_df.fillna(1E18)
        
        
        df_Funza[f'{i}'] = pivot_df

    df_Cedi_C= {}
    for col_name in o:
        df_filtrado = df_CC_C.loc[:, [df_CC_C.columns[0], col_name]]
        df_filtrado.index = df_filtrado['Cedi']
        df_filtrado = df_filtrado.drop(columns=['Cedi'])
        df_Cedi_C[f'{col_name}'] = df_filtrado

    df_Cedi_F= {}
    for col_name in o:
        df_filtrado = df_CC_C_F.loc[:, [df_CC_C_F.columns[0], col_name]]
        df_filtrado.index = df_filtrado['Cedi']
        df_filtrado = df_filtrado.drop(columns=['Cedi'])
        df_Cedi_F[f'{col_name}'] = df_filtrado

    df_CC_C_V.iloc[:, 1:] = df_CC_C_V.iloc[:, 1:].replace(0, 1E9)
    df_Cedi_CV= {}
    for col_name in o:
        df_filtrado = df_CC_C_V.loc[:, [df_CC_C_V.columns[0], col_name]]
        df_filtrado.index = df_filtrado['Cedi']
        df_filtrado = df_filtrado.drop(columns=['Cedi'])
        df_Cedi_CV[f'{col_name}'] = df_filtrado

    df_flete_CV2= {}
    for i in o:
        if not isinstance(i, list):
            e = [i]
        df_Flete_S["Cedi"] = df_Flete_S["Cedi"].astype(str).str.strip()
        df_filtrado = df_Flete_S[df_Flete_S["Tipo_Transporte"].isin(e)].drop(columns=['ID','Tipo_Transporte', 'Eliminar'])
        pivot_df = df_filtrado.pivot(index='Cedi', columns='Destino', values='Flete')
        pivot_df = pivot_df.fillna(1E9)
        df_flete_CV2[f'{i}'] = pivot_df

    df_bog = {}
    for i in o:
        if not isinstance(i, list):
            e = [i]
        df_Flete_S["Cedi"] = df_Flete_S["Cedi"].astype(str).str.strip()
        df_filtrado = df_Flete_S[df_Flete_S["Tipo_Transporte"].isin(e) & (df_Flete_S["Cedi"] == "Pta_BOG")].drop(columns=['ID','Tipo_Transporte', 'Eliminar'])
        pivot_df = df_filtrado.pivot(index='Cedi', columns='Destino', values='Flete')
        pivot_df = pivot_df.fillna(1E9)
        df_bog[f'{i}'] = pivot_df

    df_demanda = {}
    for i in o:
        pro = list(productos[i])
        dep = ["DEPTO_RED"]
        lista = dep + pro  
        df_filtrado = df_D[lista]
        df_filtrado.index = df_filtrado['DEPTO_RED']
        df_filtrado = df_filtrado.drop(columns=['DEPTO_RED'])
        df_demanda[f'{i}'] = df_filtrado

    for i in o: 
        if i == "Seco":
            n = df_demanda[i].index.tolist()
            e = df_bog[i].columns.tolist()  # Corrected this line
            buscar = [elemento for elemento in n if elemento not in e]  # Corrected this line

            df_bog[i][buscar] = 1E18  # Corrected this line

    for i in o:
        if i == "Seco":
            n = df_Cedi_C[i].index.tolist()
            e = df_bog[i].index.tolist()  # Corrected this line
            buscar = [elemento for elemento in n if elemento not in e]  # Corrected this line

            # Create new rows in df_bog for elements in 'buscar'
            for elemento in buscar:
                df_bog[i].loc[elemento] = 1E18  # Corrected this line

    for i in productos:
        n = df_planta_C[i].columns.tolist()
        e = df_flete_CV[i].index.tolist()

        elementos_F = [final for final in n if not final in e]
        df_planta_C[i] = df_planta_C[i].drop(columns=elementos_F)
        df_planta_CF[i] = df_planta_CF[i].drop(columns=elementos_F)
        df_planta_CV[i] = df_planta_CV[i].drop(columns=elementos_F)

    df_flete_CV["Seco"]["Pta_BOG"] = 1E18 #penalización de flete de costo variable en la planta de bogotá
    for i in productos:
        n = df_Cedi_C[i].index.tolist()
        e = df_flete_CV[i].columns.tolist()
        elementos_F = [final for final in n if not final in e]
        df_Cedi_C[i] = df_Cedi_C[i].drop(index=elementos_F)
        df_Cedi_F[i] = df_Cedi_F[i].drop(index=elementos_F)
        df_Cedi_CV[i] = df_Cedi_CV[i].drop(index=elementos_F)

    df_flete_CV["Seco"].loc["Pta_BOG","Pta_BOG"] = 0 # para que sepa que entre lo que produce bogota y lo que entrega a clientes
    df_Cedi_C["Seco"].loc["Pta_BOG","Seco"] = 1E18 #Penalización 


    x_ijk = {} #Variable de decisión 



    for d in o:
        var_name = LpVariable.dicts(f"{d}_ijk", (productos[d], df_flete_CV[d].index, df_Cedi_F[d].index) , lowBound=0 , cat = "Continuous")
        x_ijk[f"{d}"] = var_name

    for i in productos:
        n = df_demanda[i].index.tolist()
        e = df_flete_CV2[i].columns.tolist()
        elementos_F = [final for final in n if not final in e]
        df_demanda[i] = df_demanda[i].drop(index=elementos_F)

 
    y_ikl = {}
    for d in o:
        var_name = LpVariable.dicts(f"{d}_ikl", ( productos[d], df_Cedi_C[d].index, df_demanda[d].index ) , lowBound=0 , cat = "Continuous")
        y_ikl[f"{d}"] = var_name



    b_ij = {}
    for i in productos:
        var_name = pulp.LpVariable.dicts(f"b_ij{i}", (productos[i], df_flete_CV[i].index), cat="Binary")
        b_ij[f"{i}"] = var_name

    b_k = {}
    for i in productos:
        var_name = pulp.LpVariable.dicts(f"b_k{i}", (df_flete_CV[i].columns), cat="Binary")
        b_k[f"{i}"] = var_name


    for i in productos:
        if i in ["Refrigerado","Seco"]:
            n = df_Cedi_C[i].index.tolist()
            e = df_Funza[i].columns.tolist()

            buco = [final for final in n if not final in e]

            df_Funza[i][buco] = 1E18

    funza = {}

    for i in productos:
        if i in ["Refrigerado","Seco"]:
            var_name = LpVariable.dicts(f"{i}_ik", (productos[i], df_Cedi_F[i].index) , lowBound=0 , cat = "Continuous")
            funza[f"{i}"] = var_name


    df_Funza["Refrigerado"].loc["FUNZA","FUNZA"] = 0
    df_Funza["Seco"].loc["FUNZA","FUNZA"] = 0

    fun = 0
    for a in productos:
        fun += pulp.lpSum(x_ijk[a][i][j][k] * df_planta_CV[a].loc[i, j] for i in productos[a] for j in df_flete_CV[a].index for k in df_Cedi_F[a].index)
        fun += pulp.lpSum(x_ijk[a][i][j][k] * df_Cedi_CV[a].loc[k, a] for i in productos[a] for j in df_flete_CV[a].index for k in df_Cedi_CV[a].index)
        fun += pulp.lpSum(x_ijk[a][i][j][k] * df_flete_CV[a].loc[j, k] for i in productos[a] for j in df_flete_CV[a].index for k in df_Cedi_F[a].index)
        fun += pulp.lpSum(b_ij[a][i][j] * df_planta_CF[a].loc[i, j] for i in productos[a] for j in df_flete_CV[a].index)
        fun += pulp.lpSum(b_k[a][k] * df_Cedi_F[a].loc[k, a] for k in df_Cedi_CV[a].index)

    for a in productos: 
        fun+= pulp.lpSum(y_ikl[a][i][k][l]*df_flete_CV2[a].loc[k,l] for i in productos[a] for k in df_Cedi_C[a].index for l in df_demanda[a].index)

    for a in productos:
        if a in ["Refrigerado","Seco"]:
            fun += pulp.lpSum(funza[a][i][k]*df_Cedi_CV[a].loc[k,a] for i in productos[a] for k in df_Cedi_F[a].index)

    for a in productos:
        if a in ["Refrigerado","Seco"]:
            fun += pulp.lpSum(funza[a][i][k]*df_Funza[a].loc["FUNZA",k] for i in productos[a] for k in df_Cedi_F[a].index)

    
    Empresa = LpProblem("Minimizar_Empresa", LpMinimize)
    Empresa += fun


    for a in productos: 
        for i in productos[a]:
            for j in df_planta_C[a].columns:
                if i not in ["Canola", "Girasol","Vegetales"]:
                    Empresa+= lpSum(x_ijk[a][i][j][k] for k in df_Cedi_F[a].index ) <= df_planta_C[a].loc[i,j]


    for j in df_planta_CF["Seco"].columns:
        Empresa+= lpSum(x_ijk["Seco"][i][j][k] for i in productos[a] if i in ["Canola", "Girasol","Vegetales"] for k in df_Cedi_F[a].index ) <= df_planta_C["Seco"].loc["Vegetales",j]


    for a in productos:
        for k in df_Cedi_C[a].index:
            if a in ["Refrigerado","Seco"] and k != "FUNZA":
                Empresa+= lpSum(x_ijk[a][i][j][k] for i in productos[a] for j in df_flete_CV[a].index) + pulp.lpSum(funza[a][i][k] for i in productos[a]) <= df_Cedi_C[a].loc[k,a]*3
            else: 
                Empresa+= lpSum(x_ijk[a][i][j][k] for i in productos[a] for j in df_flete_CV[a].index) <= df_Cedi_C[a].loc[k,a]*3

    
    for a in productos:
        for i in productos[a]:
            for l in df_demanda[a].index:
                Empresa+= lpSum(y_ikl[a][i][k][l] for k in df_Cedi_F[a].index) >= df_demanda[a].loc[l,i]

    
    for a in productos:
        for k in df_Cedi_C[a].index:
            for i in productos[a]:
                if a in ["Refrigerado","Seco"]:
                    Empresa+= lpSum(x_ijk[a][i][j][k]  for j in df_flete_CV[a].index ) + lpSum(funza[a][i][k]) ==  lpSum(y_ikl[a][i][k][l] for l in df_demanda[a].index)
                else:
                    Empresa+= lpSum(x_ijk[a][i][j][k]  for j in df_flete_CV[a].index) ==  lpSum(y_ikl[a][i][k][l] for l in df_demanda[a].index)
    

    for a in productos:
        for i in productos[a]:
            if a =="Seco":
                Empresa += lpSum(x_ijk[a][i]["Pta_BOG"][k]  for k in df_Cedi_F[a].index) - lpSum(y_ikl[a][i]["Pta_BOG"][l] for l in df_demanda[a].index)  == lpSum(funza[a][i][k] for k in df_Cedi_F[a].index)
            if a =="Refrigerado":
                Empresa += lpSum(x_ijk[a][i]["Pta_BOG"][k]  for k in df_Cedi_F[a].index) == lpSum(funza[a][i][k] for k in df_Cedi_F[a].index)
    
    for a in productos:
        for j in df_flete_CV[a].index:
            for i in productos[a]:
                Empresa += lpSum(x_ijk[a][i][j][k] for k in df_Cedi_C[a].index) <= b_ij[a][i][j]*1E8

    for a in productos:
        for k in df_Cedi_F[a].index:
            if i in ["Refrigerado","Seco"]:
                Empresa += lpSum(x_ijk[a][i][j][k] for i in productos[a] for j in df_flete_CV[a].index) +  lpSum(funza[a][i][k] for i in productos[a])  <= b_k[a][k]*1E8
            else:
                Empresa += lpSum(x_ijk[a][i][j][k] for i in productos[a] for j in df_flete_CV[a].index)  <= b_k[a][k]*1E8
    
    Empresa.solve()
        
    variables_normales = []
    variables_binarias = []

    for variable in Empresa.variables():
        valor = variable.varValue
        # Filtrar variables mayores a cero
        if valor and valor > 0:
            if variable.cat == "Binary":
                variables_binarias.append((variable.name, valor))
            else:
                variables_normales.append((variable.name, valor))

    # Ruta para guardar el archivo
    output_path = filedialog.asksaveasfilename(
        title="Guardar resultados",
        defaultextension=".txt",
        filetypes=[("Archivo de texto", "*.txt")]
    )

    if output_path:
        with open(output_path, "w") as f:
            f.write("Variables Normales Mayores a Cero:\n")
            for name, value in variables_normales:
                f.write(f"{name}: {value}\n")

            f.write("\nVariables Binarias Mayores a Cero:\n")
            for name, value in variables_binarias:
                f.write(f"{name}: {value}\n")

        print(f"Resultados guardados en: {output_path}")


except Exception as e:
    error_message = traceback.format_exc()
    log_error_to_file(error_message)

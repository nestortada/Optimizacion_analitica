import sqlite3
import pandas as pd
import os


def update_progress(step, total_steps,progress_bar,progress_window):
    progress = (step / total_steps) * 100
    progress_bar['value'] = progress
    progress_window.update_idletasks()

def vistasM_F_Capacidad(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    Descripciones_query = "SELECT DISTINCT Descripcion FROM plantas"
    Descripciones_df = pd.read_sql_query(Descripciones_query, conn)
    Descripciones = Descripciones_df['Descripcion'].tolist()  
    select_clause = "SELECT Agrupaciones"
    for Descripcion in Descripciones:
        select_clause += f", SUM(CASE WHEN Ciudad = '{Descripcion}' THEN Capacidad ELSE 0 END) AS {Descripcion}"
    query = f"""
    {select_clause}
    FROM capacidad_lineas
    GROUP BY Agrupaciones;
    """
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    df_result.to_csv(os.path.join(directory, 'df_CL_C.csv'), index=False)

def vistasM_F_Costos_Fijos(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    Descripciones_query = "SELECT DISTINCT Descripcion FROM plantas"
    Descripciones_df = pd.read_sql_query(Descripciones_query, conn)
    Descripciones = Descripciones_df['Descripcion'].tolist()  
    select_clause = "SELECT Agrupaciones"
    for Descripcion in Descripciones:
        select_clause += f", SUM(CASE WHEN Ciudad = '{Descripcion}' THEN Costo_Fijo ELSE 0 END) AS {Descripcion}"
    query = f"""
    {select_clause}
    FROM capacidad_lineas
    GROUP BY Agrupaciones;
    """
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    df_result.to_csv(os.path.join(directory, 'df_CL_C_F.csv'), index=False)

def vistasM_F_Costos_Variables(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    Descripciones_query = "SELECT DISTINCT Descripcion FROM plantas"
    Descripciones_df = pd.read_sql_query(Descripciones_query, conn)
    Descripciones = Descripciones_df['Descripcion'].tolist()  
    select_clause = "SELECT Agrupaciones"
    for Descripcion in Descripciones:
        select_clause += f", SUM(CASE WHEN Ciudad = '{Descripcion}' THEN Costo_Variable ELSE 0 END) AS {Descripcion}"
    query = f"""
    {select_clause}
    FROM capacidad_lineas
    GROUP BY Agrupaciones;
    """
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    df_result.to_csv(os.path.join(directory, 'df_CL_C_V.csv'), index=False)

def vistaFlete_Primario_capacidad(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    Fletes_secundarios_query = "SELECT * FROM fletes_primarios"
    Fletes_secundarios_df = pd.read_sql_query(Fletes_secundarios_query, conn)
    conn.close()
    Fletes_secundarios_df.to_csv(os.path.join(directory, 'df_Flete_P.csv'), index=False)


def Vista_Capacidad_cedi(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    almacenamiento_query = "SELECT DISTINCT Tipo_Almacenamiento FROM capacidad_cedis"
    almacenamiento_df = pd.read_sql_query(almacenamiento_query, conn)
    almacenamientos = almacenamiento_df['Tipo_Almacenamiento'].tolist()
    select_clause = "SELECT Cedi"
    for almacenamiento in almacenamientos:
        select_clause += f", SUM(CASE WHEN Tipo_Almacenamiento = '{almacenamiento}' THEN Capacidad ELSE 0 END) AS '{almacenamiento}'"

    query = f"""
    {select_clause}
    FROM capacidad_cedis
    GROUP BY Cedi;
    """
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    df_result.to_csv(os.path.join(directory, 'df_CC_C.csv'), index=False)

def Vista_Costo_Fijo_Cedi(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    almacenamiento_query = "SELECT DISTINCT Tipo_Almacenamiento FROM capacidad_cedis"
    almacenamiento_df = pd.read_sql_query(almacenamiento_query, conn)
    almacenamientos = almacenamiento_df['Tipo_Almacenamiento'].tolist()
    select_clause = "SELECT Cedi"
    for almacenamiento in almacenamientos:
        select_clause += f", SUM(CASE WHEN Tipo_Almacenamiento = '{almacenamiento}' THEN Costo_Fijo ELSE 0 END) AS '{almacenamiento}'"

    query = f"""
    {select_clause}
    FROM capacidad_cedis
    GROUP BY Cedi;
    """
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    df_result.to_csv(os.path.join(directory, 'df_CC_C_F.csv'), index=False)


def Vista_Costo_Variable_Cedi(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    almacenamiento_query = "SELECT DISTINCT Tipo_Almacenamiento FROM capacidad_cedis"
    almacenamiento_df = pd.read_sql_query(almacenamiento_query, conn)
    almacenamientos = almacenamiento_df['Tipo_Almacenamiento'].tolist()
    select_clause = "SELECT Cedi"
    for almacenamiento in almacenamientos:
        select_clause += f", SUM(CASE WHEN Tipo_Almacenamiento = '{almacenamiento}' THEN Costo_variable ELSE 0 END) AS '{almacenamiento}'"

    query = f"""
    {select_clause}
    FROM capacidad_cedis
    GROUP BY Cedi;
    """
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    df_result.to_csv(os.path.join(directory, 'df_CC_C_V.csv'), index=False)

def Vista_Flete_Secundario_Capacidad(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    Fletes_secundarios_query = "SELECT * FROM fletes_secundarios"
    Fletes_secundarios_df = pd.read_sql_query(Fletes_secundarios_query, conn)
    conn.close()
    Fletes_secundarios_df.to_csv(os.path.join(directory, 'df_Flete_S.csv'), index=False)

def Vista_Demanda(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    Resumen_query = "SELECT DISTINCT Tipo_Resumen FROM demanda"
    Resumen_df = pd.read_sql_query(Resumen_query, conn)
    Resumen = Resumen_df['Tipo_Resumen'].tolist()
    select_clause = "SELECT DEPTO_RED"
    for Resum in Resumen:
        select_clause += f", SUM(CASE WHEN Tipo_Resumen = '{Resum}' THEN Total ELSE 0 END) AS '{Resum}'"

    query = f"""
    {select_clause}
    FROM demanda
    GROUP BY DEPTO_RED;
    """
    df_result = pd.read_sql_query(query, conn)
    conn.close()
    df_result.to_csv(os.path.join(directory, 'df_D.csv'), index=False)

def vistaMateriales(conectar,directory):
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(conectar)
    materiales_query = "SELECT * FROM materiales"
    materiales_df = pd.read_sql_query(materiales_query, conn)
    conn.close()
    materiales_df.to_csv(os.path.join(directory, 'df_materiales.csv'), index=False)


def create_allV(conectar,current_step, total_steps,progress_bar,progress_window,directory):
    current_step = current_step
    vistasM_F_Capacidad(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    vistasM_F_Costos_Fijos(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    vistasM_F_Costos_Variables(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    vistaFlete_Primario_capacidad(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    Vista_Capacidad_cedi(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    Vista_Costo_Fijo_Cedi(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    Vista_Costo_Variable_Cedi(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    Vista_Flete_Secundario_Capacidad(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    Vista_Demanda(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    vistaMateriales(conectar,directory)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    return current_step

if __name__ == "__main__": 
    pass

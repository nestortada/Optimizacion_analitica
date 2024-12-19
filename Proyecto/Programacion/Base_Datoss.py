import sqlite3 as sql
import pandas as pd
from tkinter import messagebox


def update_progress(step, total_steps,progress_bar,progress_window):
    progress = (step / total_steps) * 100
    progress_bar['value'] = progress
    progress_window.update_idletasks()



def createDB(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error en la creación de la base de datos: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()



def createTableCliente(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
                           ID INTEGER PRIMARY KEY,
                           DEPTO_RED TEXT NOT NULL UNIQUE,
                           PAIS TEXT NOT NULL CHECK(PAIS IN ('COLOMBIA', 'OTROS')),
                           Tipo_Cliente TEXT NOT NULL CHECK(Tipo_Cliente IN ('Nacional', 'Exportacion')),
                           Latitud TEXT,
                           Longitud TEXT,
                           Problema TEXT
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de clientes: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def insertInfoClientes(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Clientes")
        df.rename(columns={'DEPTO RED': 'DEPTO_RED'}, inplace=True)
        df = df[['ID', 'DEPTO_RED', 'PAIS', 'Tipo_Cliente', 'Latitud', 'Longitud', 'Problema']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes")  
        conn.commit()
        
        df.to_sql('clientes', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de clientes: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def createTableDemanda(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS demanda(
                           ID INTEGER PRIMARY KEY,
                           DEPTO_RED TEXT NOT NULL,
                           Tipo_Resumen TEXT NOT NULL,
                           Total INTEGER NOT NULL,
                           Eliminar TEXT,
                           FOREIGN KEY ("DEPTO_RED") REFERENCES "clientes"("DEPTO_RED"),
                           FOREIGN KEY ("Tipo_Resumen") REFERENCES "materiales"("Agrupaciones")
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de demanda: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def insertInfoDemanda(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Demanda", nrows=246)
        df.rename(columns={'DEPTO RED': 'DEPTO_RED', 'Tipo Resumen': 'Tipo_Resumen'}, inplace=True)
        df['Total'] = df['Total'].astype(str).str.replace(',', '').astype(float).astype(int)
        df = df[['ID', 'DEPTO_RED', 'Tipo_Resumen', 'Total', 'Eliminar']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM demanda")  
        conn.commit()
        
        df.to_sql('demanda', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de demanda: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def createTableMateriales(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS materiales(
                           ID INTEGER PRIMARY KEY,
                           Agrupaciones TEXT NOT NULL UNIQUE,
                           Tipo_Almacenamiento TEXT NOT NULL,
                           Tipo_Transporte TEXT NOT NULL,
                           Problema TEXT
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de materiales: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def insertInfoMateriales(path,db_path): 
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Materiales")
        df.rename(columns={'Tipo transporte': 'Tipo_Transporte'}, inplace=True)
        df = df[['ID', 'Agrupaciones', 'Tipo_Almacenamiento', 'Tipo_Transporte', 'Problema']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM materiales")  
        conn.commit()
        
        df.to_sql('materiales', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de materiales: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def createTablePlantas(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS plantas(
                           ID INTEGER PRIMARY KEY,
                           Descripcion TEXT NOT NULL UNIQUE,
                           Direccion TEXT NOT NULL UNIQUE,
                           Ciudad TEXT NOT NULL,
                           Departamento TEXT NOT NULL,
                           Latitud TEXT,
                           Longitud TEXT,
                           Problema TEXT
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de plantas: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()



def insertInfoPlantas(path,db_path): 
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Plantas")
        df.rename(columns={'Descripción ': 'Descripcion', 'Dirección': 'Direccion'}, inplace=True)
        df = df[['ID', 'Descripcion', 'Direccion', 'Ciudad', 'Departamento', 'Latitud', 'Longitud', 'Problema']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM plantas")  
        conn.commit()
        
        df.to_sql('plantas', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de plantas: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def createTableCapacidad_Lineas(db_path): 
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS capacidad_lineas(
                           ID INTEGER PRIMARY KEY,
                           Descripcion_Linea TEXT NOT NULL,
                           Ciudad TEXT NOT NULL,
                           Departamento TEXT NOT NULL,
                           Capacidad INTEGER NOT NULL,
                           Costo_Fijo INTEGER NOT NULL,
                           Costo_Variable INTEGER NOT NULL,
                           Agrupaciones TEXT NOT NULL,
                           Eliminar TEXT,
                           FOREIGN KEY ("Agrupaciones") REFERENCES "materiales"("Agrupaciones")
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de capacidad de líneas: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def insertInfoCapacidad_Lineas(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Capacidad Lineas")
        df.rename(columns={'Descripción Linea': 'Descripcion_Linea'}, inplace=True)
        df = df[['ID', 'Descripcion_Linea', 'Ciudad', 'Departamento', 'Capacidad', 'Costo_Fijo', 'Costo_Variable', 'Agrupaciones', 'Eliminar']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM capacidad_lineas")  
        conn.commit()
        
        df.to_sql('capacidad_lineas', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de capacidad de líneas: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()



def createTableCedis(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS cedis(
                           ID INTEGER PRIMARY KEY,
                           ID_Interno TEXT NOT NULL UNIQUE,
                           Descripcion TEXT NOT NULL,
                           Direccion TEXT NOT NULL UNIQUE,
                           Ciudad TEXT NOT NULL,
                           Departamento TEXT NOT NULL,
                           Latitud TEXT,
                           Longitud TEXT,
                           Problema TEXT
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de CEDIS: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def insertInfoCedis(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Cedis")
        df.rename(columns={'ID interno': 'ID_Interno', 'Descripción ': 'Descripcion', 'Dirección': 'Direccion'}, inplace=True)
        df = df[['ID', 'ID_Interno', 'Descripcion', 'Direccion', 'Ciudad', 'Departamento', 'Latitud', 'Longitud', 'Problema']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cedis")  
        conn.commit()
        
        df.to_sql('cedis', conn, if_exists='append', index=False)  
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de CEDIS: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def CreateTableOrigen(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS origenes(
                           ID INTEGER PRIMARY KEY,
                           Origen TEXT NOT NULL,
                           Problema TEXT
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de orígenes: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def insertInfoOrigenes(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Origen")
        df = df[["ID", "Origen", "Problema"]]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM origenes")
        conn.commit()
        
        df.to_sql("origenes", conn, if_exists="append", index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de orígenes: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def createTableFletes_Primarios(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS fletes_primarios(
                           ID INTEGER PRIMARY KEY,
                           Origen TEXT NOT NULL,
                           Destino TEXT NOT NULL,
                           Tipo_Transporte TEXT NOT NULL,
                           Flete INTEGER NOT NULL,
                           Eliminar TEXT,
                           FOREIGN KEY ("Origen") REFERENCES "origenes"("Origen")
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de fletes primarios: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()


def insertInfoFletes_Primarios(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Fletes_Primarios")
        df['ID'] = df.index
        df = df[['ID', 'Origen', 'Destino', 'Tipo_Transporte', 'Flete', 'Eliminar']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM fletes_primarios")  
        conn.commit()
        
        df.to_sql('fletes_primarios', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de fletes primarios: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def createTableCapacidad_Cedis(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS capacidad_cedis(
                           ID INTEGER PRIMARY KEY,
                           ID_Cedi TEXT NOT NULL,
                           Descripcion_Cedi TEXT NOT NULL UNIQUE,
                           Tipo_Almacenamiento TEXT NOT NULL,
                           Cedi TEXT NOT NULL,
                           Ciudad TEXT NOT NULL,
                           Departamento TEXT NOT NULL,
                           Capacidad INTEGER NOT NULL,
                           Costo_Fijo INTEGER NOT NULL,
                           Costo_Variable INTEGER NOT NULL,
                           Eliminar TEXT,
                           FOREIGN KEY ("ID_Cedi") REFERENCES "cedis"("ID_Interno")
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de capacidad de CEDIS: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def insertInfoCapacidad_Cedis(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Capacidad Cedis")
        df.rename(columns={'ID': 'ID_Cedi', 'Descripción Cedi': 'Descripcion_Cedi', 'Costo_Fijo (Mes)': 'Costo_Fijo', 'Costo_Variable (Posición)': 'Costo_Variable'}, inplace=True)
        df['ID'] = df.index
        df['Costo_Fijo'] = df['Costo_Fijo'].astype(str).str.replace(',', '').fillna(0).astype(float).fillna(0).astype(int)
        df['Costo_Variable'] = df['Costo_Variable'].astype(str).str.replace(',', '').fillna(0).astype(float).fillna(0).astype(int)
        df = df[['ID', 'ID_Cedi', 'Descripcion_Cedi', 'Tipo_Almacenamiento', 'Cedi', 'Ciudad', 'Departamento', 'Capacidad', 'Costo_Fijo', 'Costo_Variable', 'Eliminar']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM capacidad_cedis")  
        conn.commit()
        
        df.to_sql('capacidad_cedis', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de capacidad de CEDIS: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def createTableFletes_Secundarios(db_path):
    conn = None
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS fletes_secundarios(
                           ID INTEGER PRIMARY KEY,
                           Cedi TEXT NOT NULL,
                           Destino TEXT NOT NULL,
                           Tipo_Transporte TEXT NOT NULL,
                           Flete INTEGER NOT NULL,
                           Eliminar TEXT,
                           FOREIGN KEY ("Cedi") REFERENCES "capacidad_cedis"("Cedi"),
                           FOREIGN KEY ("Destino") REFERENCES "clientes"("DEPTO_RED")
                           )""")
        conn.commit()
    except sql.Error as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al crear la tabla de fletes secundarios: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def insertInfoFletes_Secundarios(path,db_path):
    conn = None
    try:
        df = pd.read_excel(path, sheet_name="Fletes_Secundarios")
        df['ID'] = df.index
        df['Flete'] = df['Flete'].astype(str).str.replace(',', '').fillna(0).astype(float).fillna(0).astype(int)
        df = df[['ID', 'CEDI', 'Destino', 'Tipo_Transporte', 'Flete', 'Eliminar']]
        
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM fletes_secundarios")  
        conn.commit()
        
        df.to_sql('fletes_secundarios', conn, if_exists='append', index=False)
        conn.commit()
    except (sql.Error, pd.errors.EmptyDataError, pd.errors.ClosedFileError) as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al insertar la información de fletes secundarios: {e}. Si necesitas solucionar, llama al 322-3149327")
    finally:
        if conn:
            conn.close()

def create_allDB(path,db_path,progress_bar,progress_window,total_steps,current_step):
    current_step = current_step
    createDB(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableCliente(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableMateriales(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTablePlantas(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableCedis(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    CreateTableOrigen(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableDemanda(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableCapacidad_Lineas(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableFletes_Primarios(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableCapacidad_Cedis(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    createTableFletes_Secundarios(db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoOrigenes(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoMateriales(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoClientes(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoCedis(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoPlantas(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoCapacidad_Cedis(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoCapacidad_Lineas(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoDemanda(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoFletes_Primarios(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)

    insertInfoFletes_Secundarios(path,db_path)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    return current_step


if __name__ =="__main__":
    pass
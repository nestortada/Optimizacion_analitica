import sqlite3 as sql


def update_progress(step, total_steps,progress_bar,progress_window):
    progress = (step / total_steps) * 100
    progress_bar['value'] = progress
    progress_window.update_idletasks()


# 1 Cliente

def createTableEliminadosClientes(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes_eliminados(
                   ID INTEGER,
                   DEPTO_RED TEXT,
                   PAIS TEXT,
                   Tipo_Cliente TEXT,
                   Latitud TEXT,
                   Longitud TEXT,
                   Problema TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()

def createTriggerClientes(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_clientes
                      BEFORE DELETE ON clientes
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO clientes_eliminados (ID, DEPTO_RED, PAIS, Tipo_Cliente, Latitud, Longitud, Problema)
                          VALUES (OLD.ID, OLD.DEPTO_RED, OLD.PAIS, OLD.Tipo_Cliente, OLD.Latitud, OLD.Longitud, OLD.Problema);
                      END;""")
    conn.commit()
    conn.close()


def EliminarInfoClientes(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE Problema = 1")
    conn.commit()
    conn.close()

# 2 Demanda

def createTableEliminadosDemanda(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS demanda_eliminados(
                   ID INTEGER,
                   DEPTO_RED TEXT,
                   Tipo_Resumen TEXT,
                   Total INTEGER,
                   Eliminar TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()

def createTriggerDemanda(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_demanda
                      BEFORE DELETE ON demanda
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO demanda_eliminados (ID, DEPTO_RED, Tipo_Resumen, Total, Eliminar)
                          VALUES (OLD.ID, OLD.DEPTO_RED, OLD.Tipo_Resumen, OLD.Total, OLD.Eliminar);
                      END;""")
    conn.commit()
    conn.close()



def EliminarInfoDemanda(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM demanda WHERE Eliminar = 1")
    conn.commit()
    conn.close()


# 3 Materiales

def createTableEliminadosMateriales(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS materiales_eliminados(
                   ID INTEGER,
                   Agrupaciones TEXT,
                   Tipo_Almacenamiento TEXT,
                   Tipo_Transporte TEXT,
                   Problema TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()

def createTriggerMateriales(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_materiales
                      BEFORE DELETE ON materiales
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO materiales_eliminados (ID, Agrupaciones, Tipo_Almacenamiento, Tipo_Transporte, Problema)
                          VALUES (OLD.ID, OLD.Agrupaciones, OLD.Tipo_Almacenamiento, OLD.Tipo_Transporte, OLD.Problema);
                      END;""")
    conn.commit()
    conn.close()


def EliminarInfoMateriales(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM materiales WHERE Problema = 1")
    conn.commit()
    conn.close()

# 4 Plantas


def createTableEliminadosPlantas(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS plantas_eliminados(
                   ID INTEGER,
                   Descripcion TEXT,
                   Direccion TEXT,
                   Ciudad TEXT,
                   Departamento TEXT,
                   Latitud TEXT,
                   Longitud TEXT,
                   Problema TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()


def createTriggerPlantas(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_plantas
                      BEFORE DELETE ON plantas
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO plantas_eliminados (ID, Descripcion, Direccion, Ciudad, Departamento, Latitud, Longitud, Problema)
                          VALUES (OLD.ID, OLD.Descripcion, OLD.Direccion, OLD.Ciudad, OLD.Departamento, OLD.Latitud, OLD.Longitud, OLD.Problema);
                      END;""")
    conn.commit()
    conn.close()

def EliminarInfoPlantas(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM plantas WHERE Problema = 1")
    conn.commit()
    conn.close()

# 5 Cedis

def createTableEliminadosCedis(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cedis_eliminados(
                   ID INTEGER,
                   ID_Interno TEXT,
                   Descripcion TEXT,
                   Direccion TEXT,
                   Ciudad TEXT,
                   Departamento TEXT,
                   Latitud TEXT,
                   Longitud TEXT,
                   Problema TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()


def createTriggerCedis(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_cedis
                      BEFORE DELETE ON cedis
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO cedis_eliminados (ID, ID_Interno, Descripcion, Direccion, Ciudad, Departamento, Latitud, Longitud, Problema)
                          VALUES (OLD.ID, OLD.ID_Interno, OLD.Descripcion, OLD.Direccion, OLD.Ciudad, OLD.Departamento, OLD.Latitud, OLD.Longitud, OLD.Problema);
                      END;""")
    conn.commit()
    conn.close()




def EliminarInfoCedis(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cedis WHERE Problema = 1")
    conn.commit()
    conn.close()

# 6 Origenes


def createTableEliminadosOrigenes(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS origenes_eliminados(
                   ID INTEGER,
                   Origen TEXT,
                   Problema TEXT
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()

def createTriggerOrigenes(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_origenes
                      BEFORE DELETE ON origenes
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO origenes_eliminados (ID, Origen, Problema)
                          VALUES (OLD.ID, OLD.Origen, OLD.Problema);
                      END;""")
    conn.commit()
    conn.close()

def EliminarInfoOrigenes(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM origenes WHERE Problema = 1")
    conn.commit()
    conn.close()

#7 Capacidad de linea 


def createTableEliminadosCapacidadLineas(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS capacidad_lineas_eliminados(
                   ID INTEGER,
                   Descripcion_Linea TEXT,
                   Ciudad TEXT,
                   Departamento TEXT,
                   Capacidad INTEGER,
                   Costo_Fijo INTEGER,
                   Costo_Variable INTEGER,
                   Agrupaciones TEXT,
                   Eliminar TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()


def createTriggerCapacidadLineas(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_capacidad_lineas
                      BEFORE DELETE ON capacidad_lineas
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO capacidad_lineas_eliminados (ID,Descripcion_Linea,Ciudad,Departamento,Capacidad,Costo_Fijo,Costo_Variable,Agrupaciones,Eliminar)
                          VALUES (OLD.ID, OLD.Descripcion_Linea, OLD.Ciudad, OLD.Departamento, OLD.Capacidad, OLD.Costo_Fijo, OLD.Costo_Variable,OLD.Agrupaciones,OLD.Eliminar);
                      END;""")
    conn.commit()
    conn.close()


def EliminarInfoCapacidad_Linea(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM capacidad_lineas WHERE Eliminar = 1")
    conn.commit()
    conn.close()

# 8 Flete Primario 

def createTableEliminadosFletePrimario(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS flete_primario_eliminados(
                   ID INTEGER,
                   Origen TEXT,
                   Destino TEXT,
                   Tipo_Transporte TEXT,
                   Flete INTEGER,
                   Eliminar TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()

def createTriggerFletePrimario(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_flete_primario
                      BEFORE DELETE ON fletes_primarios
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO flete_primario_eliminados (ID, Origen, Destino, Tipo_Transporte, Flete,Eliminar)
                          VALUES (OLD.ID, OLD.Origen, OLD.Destino, OLD.Tipo_Transporte, OLD.Flete, OLD.Eliminar);
                      END;""")
    conn.commit()
    conn.close()


def EliminarInfoFletes_Primarios(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fletes_primarios WHERE Eliminar = 1")
    conn.commit()
    conn.close()

#9 capacidad cedis

def createTableEliminadosCapacidadCedis(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS capacidad_cedis_eliminados(
                   ID INTEGER,
                   ID_Cedi INTEGER,
                   Descripcion_Cedi TEXT,
                   Tipo_Almacenamiento TEXT,
                   Cedi TEXT,
                   Ciudad TEXT,
                   Departamento TEXT,
                   Capacidad INTEGER,
                   Costo_Fijo INTEGER,
                   Costo_Variable INTEGER,
                   Eliminar TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()

def createTriggerCapacidadCedis(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_capacidad_cedis
                      BEFORE DELETE ON capacidad_cedis
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO capacidad_cedis_eliminados (ID, ID_Cedi, Descripcion_Cedi,Tipo_Almacenamiento, Cedi, Ciudad, Departamento, Capacidad,Costo_Fijo,Costo_Variable,Eliminar)
                          VALUES (OLD.ID, OLD.ID_Cedi, OLD.Descripcion_Cedi, OLD.Tipo_Almacenamiento, OLD.Cedi, OLD.Ciudad, OLD.Departamento, OLD.Capacidad, OLD.Costo_Fijo, OLD.Costo_Variable, OLD.Eliminar);
                      END;""")
    conn.commit()
    conn.close()

def EliminarInfoCapacidad_Cedis(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM capacidad_cedis WHERE Eliminar = 1")
    conn.commit()
    conn.close()

#10 Flete Secundario 

def createTableEliminadosFleteSecundario(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS flete_secundario_eliminados(
                   ID INTEGER,
                   Cedi TEXT,
                   Destino TEXT,
                   Tipo_Transporte TEXT,
                   Flete INTEGER,
                   Eliminar TEXT,
                   eliminado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )""")
    conn.commit()
    conn.close()


def createTriggerFleteSecundario(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trigger_eliminar_flete_secundario
                      BEFORE DELETE ON fletes_secundarios
                      FOR EACH ROW
                      BEGIN
                          INSERT INTO flete_secundario_eliminados (ID, Cedi, Destino, Tipo_Transporte, Flete, Eliminar)
                          VALUES (OLD.ID, OLD.Cedi, OLD.Destino, OLD.Tipo_Transporte, OLD.Flete, OLD.Eliminar);
                      END;""")
    conn.commit()
    conn.close()

def EliminarInfoFletes_Secundarios(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fletes_secundarios WHERE Eliminar = 1")
    conn.commit()
    conn.close()


def eliminarant(conectar):
    conn = sql.connect(conectar)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes_eliminados")
    cursor.execute("DELETE FROM demanda_eliminados")
    cursor.execute("DELETE FROM materiales_eliminados")
    cursor.execute("DELETE FROM plantas_eliminados")
    cursor.execute("DELETE FROM cedis_eliminados")
    cursor.execute("DELETE FROM origenes_eliminados")
    cursor.execute("DELETE FROM capacidad_lineas_eliminados")
    cursor.execute("DELETE FROM flete_primario_eliminados")
    cursor.execute("DELETE FROM capacidad_cedis_eliminados")
    cursor.execute("DELETE FROM flete_secundario_eliminados")
    conn.commit()
    conn.close()



def create_allTD(conectar, current_step,total_steps,progress_bar,progress_window):
    current_step = current_step
    createTableEliminadosClientes(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosDemanda(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosMateriales(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosPlantas(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosCedis(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosOrigenes(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosCapacidadLineas(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosFletePrimario(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosCapacidadCedis(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTableEliminadosFleteSecundario(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    eliminarant(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerClientes(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerDemanda(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerMateriales(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerPlantas(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerCedis(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerOrigenes(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerCapacidadLineas(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerFletePrimario(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerCapacidadCedis(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    createTriggerFleteSecundario(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoClientes(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoDemanda(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoMateriales(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoPlantas(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoCedis(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoOrigenes(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoCapacidad_Linea(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoFletes_Primarios(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoCapacidad_Cedis(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    EliminarInfoFletes_Secundarios(conectar)
    current_step += 1
    update_progress(current_step, total_steps,progress_bar,progress_window)
    return current_step
if __name__ == "__main__":
    pass


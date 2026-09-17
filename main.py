from funciones import (
    Crear_tabla,
    agregar_columna,
    insertar_registros,
    Consultar_Registros,
    modificar_tablas_columnas,
    Eliminar_Tablas_Columnas,
)
                
            

Marcapasos = True 
while Marcapasos == True:
    entrada = input("SGDB > ")
    validation = entrada.split()

    match validation[0]:
        case "CREAR":
            if(validation[1] == "TABLA"):
                Crear_tabla(entrada)
            elif(validation[1] == "COLUMNA"):
                agregar_columna(entrada)
        case "INSERTAR":
            insertar_registros(entrada)
        case "CONSULTAR":
            Consultar_Registros(entrada)
        case "MODIFICAR":
            modificar_tablas_columnas(entrada)
        case "ELIMINAR":
            Eliminar_Tablas_Columnas(entrada)
        case "SALIR":
            Marcapasos = False 




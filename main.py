from funciones import (
    Crear_tabla,
    agregar_columna,
    insertar_registros,
    Consultar_Registros,
    modificar_tablas_columnas,
    Eliminar_Tablas_Columnas,
)
                
            
print("SGDB Python Console")
Marcapasos = True 
while Marcapasos == True:
    entrada = input("SGDB > ")
    validation = entrada.split()

    if (validation and validation[0] == "SALIR" ):
        Marcapasos = False
    elif not validation or len(validation) == 1: 
        print("Instruccion Incorrecta")
    else:
        match validation[0]:
            case "CREAR":
                if(validation[1] == "TABLA"):
                    Crear_tabla(entrada)
                elif(validation[1] == "COLUMNA"):
                    agregar_columna(entrada)
                else:
                    print("Comando Incorrecto")
            case "INSERTAR":
                insertar_registros(entrada)
            case "CONSULTAR":
                Consultar_Registros(entrada)
            case "MODIFICAR":
                modificar_tablas_columnas(entrada)
            case "ELIMINAR":
                Eliminar_Tablas_Columnas(entrada)
            case _:
                print("Instruccion Incorrecta ")




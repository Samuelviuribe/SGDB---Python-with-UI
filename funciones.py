#sgdb

lista_tablas = []

def Crear_tabla(entrada):

    #comando_usuario = input("Instruccion de Creacion de tabla ");
    comando = entrada.split()

    #print(partes[0]+' '+partes[1]);
    #print(comando_crear)
    #print(partes[-1]);   
    
    if(len(comando) == 3):
         
        if (comando[0] == "CREAR"):
            if (comando[1] == "TABLA"):

                temp_tab = False
                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp_tab = True

                if temp_tab:
                    print("La tabla ya existe")
                else:
                    nombre_tabla = {
                        "Nombre":comando[2],
                        "Columnas":{}, 
                        "Registros":[]
                        } 
                    
                    lista_tablas.append(nombre_tabla)
                    print("Tabla creada con exito!")

        else:
            print("Comando Incorrecto En " + comando[0] +' '+ comando[1] )
    else:
        print("Entrada Incorrecta")

def agregar_columna(entrada):
        #esperar a ejecutar sentencia esperada "CREAR COLUMNA Nombre_tabla Nombre_columna Tipo_dato"
        #comando_columnas = input("Instruccion Agregar Columna :") #se guarda en comando columna

        columna = entrada.split() #se divide en elementos de la lista 
        comando_clave_agregar_columna = columna[0] + " "+ columna[1] # se separa el comando especifico

        
        if(comando_clave_agregar_columna == "CREAR COLUMNA"): #validando comando corecto
            if(len(columna)== 5 ): #longitud de comando provicional o no idk

                temp=False
                for tabla in lista_tablas: #recorriendo lista de tablas
                    if(tabla["Nombre"] == columna[2]):
                        temp = True
                        columna_repetida = bool(0)
                        for nombre_columna in tabla["Columnas"]:
                            if(nombre_columna == columna[3]):
                                columna_repetida = bool(1)
                        if(columna_repetida == True):
                            print("Columna ya existe ")
                        else:
                            tabla["Columnas"][columna[3]] = columna[4]
                            print(tabla)
                if(temp == False):
                    print("Tabla no encontrada",lista_tablas)
            else: 
                print("Instruccion Incorrecta ")
        else:
            print("Comando equivocado para agregar columna")






def modificar_tablas_columnas(entrada):
    #nothing here yet
    # MODIFICAR TABLA Nombre_Tabla Nuevo_Nombre (4)
    
    comando = entrada.split();
    
    if (len(comando) < 4):
       print("Entrada incompleta")

    elif (len(comando) == 4):
        temp=''
        if(comando[0] == "MODIFICAR"):
            if (comando[1]== "TABLA"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp= tabla
        
                if(temp != ''):
                    print("Elemento Encontrado")        
                    temp["Nombre"] = comando[3] #aqui se cambia el nombre 
                    print(lista_tablas)
                else: 
                    print("Elemento No Encontrado")

            else:
                print("Comando Incorrecto " + comando[1])
        else:
            print("Comando Incorrecto " + comando[0])

    # MODIFICAR COLUMNA Nombre_Tabla Nombre_Columna Nuevo_Nombre (5)

    elif (len(comando) == 5):

        temp_list=''
        temp_col=''

        if(comando[0] == "MODIFICAR"):
            if(comando[1] == "COLUMNA"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp_list=tabla
                

                if(temp_list == ''):
                    print("Lista no encontrada", lista_tablas)
                else:
                    for columna in temp_list["Columnas"]:
                        if(columna == comando[3]):
                            temp_col = columna

                if(temp_col == ''):
                    print("Columna no encontrada", temp_list["Columnas"])
                else:
                    temp_list["Columnas"][comando[4]] = temp_list["Columnas"].pop(temp_col)
                    print("Nombre de columna modificado con exito",lista_tablas)


        # MOFIFICAR COLUMNA Nombre_Tabla Nombre_Columna TYPE Nuevo_Nombre_Type (6)

    elif (len(comando) == 6):
         temp_list=''
         temp_col=''

         if(comando[0] == "MODIFICAR"):
            if(comando[1] == "COLUMNA"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp_list=tabla

                if(temp_list == ''):
                    print("Lista no encontrada ", lista_tablas)
                else:
                    for columna in temp_list["Columnas"]:
                        if(columna == comando[3]):
                            temp_col = columna

                if (comando[4] == "TYPE"):
                    if(temp_col == ''):
                        print("Columna no encontrada ", temp_list["Columnas"])
                    else:
                        temp_list["Columnas"][temp_col] = comando[5]
                        print("Tipo de Columna modificado con exito ", lista_tablas)
                else:
                    print("Instruccion Incorrecta" + comando[4])

                     
def Eliminar_Tablas_Columnas(entrada):
    #ELIMINAR TABLA Nombre_Tabla 

    #entrada = input("Instruccion Eliminar : ")
    comando = entrada.split();

    temp_list = ''
    temp_col = ''

    if(len(comando) == 3):
        if (comando[0] == "ELIMINAR"):
            if (comando[1] == "TABLA"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp_list = tabla

                if(temp_list == ''): #no se si en este punto temp_list es un elemento o un diccionario
                    print("No existe "+comando[2])
                else:
                    lista_tablas.remove(temp_list)
                    print(comando[2]+" Se a eliminado satisfactoriamente")
                    print(lista_tablas)

    #ELIMINAR COLUMNA Nombre_Tabla Nombre_Columna

    if(len(comando) == 4):

        if (comando[0] == "ELIMINAR"):
            if (comando[1] == "COLUMNA"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp_list = tabla

                if(temp_list == ''):
                    print(temp_list, '  Tabla no encontrada')
                else:
                    for columna in temp_list["Columnas"]:
                        if(columna == comando[3]):
                            temp_col = columna

                    if(temp_col == ''):
                        print( temp_col + " Columna no encontrada")
                    else: 
                        temp_list["Columnas"].pop(temp_col)
                        print(temp_col +" Columna eliminada satisfactoriamente")
                        print(lista_tablas)

        
    # INSERTAR EN Nombre_Tabla Nombre_Columna Registros 
def insertar_registros(entrada):
    #entrada = input("Instruccion Insertar : ")
    comando = entrada.split()

    temp_list = ''
    
    if (len(comando) == 5):
        if(comando[0] == 'INSERTAR'):
            if(comando[1] == 'EN'):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp_list = tabla   

                if(temp_list != ''):
                    
                    registro = {}
                    temp_columna= ''
                    temp_valor= ''

                    for i in range(3, len(comando),2):
                        temp_columna = comando[i]
                        temp_valor = comando[i+1]

                        if(temp_columna in temp_list["Columnas"]):
                            registro[temp_columna] = temp_valor
                         

                    if(registro == {}):
                        print("Columna no encontrada ", temp_list["Columnas"])
                    else:
                        temp_list["Registros"].append(registro)
                        print(lista_tablas)

                else:
                    print("Tabla no existe")
                    print(lista_tablas)
    else: 
        print("Entrada Incorrecta")
            

# CONSULTAR Nombre_Tabla
def Consultar_Registros(entrada):
    #entrada = input("Digite el comando consulta : ")
    comando = entrada.split()
    temp = ''   

    if(len(comando)== 2):
        if(comando[0] == "CONSULTAR" and comando[1] == "REGISTROS"):
            print("Entrada Incompleta")

        elif(comando[0] == "CONSULTAR"):

            for tabla in lista_tablas:
                if(tabla["Nombre"] == comando[1]):
                    temp = tabla

            if(temp == ''):
                print("No existe la tabla "+ comando[1])
            else:
                print(temp)
            

    elif (len(comando) == 3):
        temp_col = ''

    #CONSULTAR REGISTROS Nombre_Tabla

        if(comando[1] == "REGISTROS"):
            if(comando[0] == "CONSULTAR"):
                temp = '' 

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp = tabla

                if(temp != ''):
                    print(temp["Registros"])
                else:
                    print("Tabla no encontrada")

    #CONSULTAR Nombre_tabla Nombre_Columna
        
        if(comando[1] != "REGISTROS"):
            if(comando[0] == "CONSULTAR"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[1]):
                            temp = tabla
                        
                if(temp != ''):
                    for columna in temp["Columnas"]:
                        if(columna == comando[2]):
                            temp_col = columna

                if(temp_col != ''):
                    print(temp["Columnas"][temp_col])
                else:
                    print("Columna no encontrada")


    #CONSULTAR Nombre_tabla Nombre_Columna TYPE
    # elif (len(comando) == 4):
    #     temp_col = ''
    #     if(comando[1] != ""):
    #         if(comando[0] == "CONSULTAR"):
    #             if(comando[3] == "TYPE"):
    #                 for tabla in lista_tablas:
    #                     if(tabla["Nombre"] == comando[1]):
    #                         temp = tabla

    #                 for columna in temp["Columnas"]:
    #                     if(columna == comando[2]):
    #                         temp_col = columna

    #                 if( temp_col== comando[2]):
    #                     print(temp["Columnas"][temp_col]) 
    
    else:
        print("Comando incorrecto")

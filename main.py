#sgdb

lista_tablas = []


def agregar_columna():
        #esperar a ejecutar sentencia esperada "CREAR COLUMNA Nombre_tabla Nombre_columna Tipo_dato"
        comando_columnas = input("Siguiente Instruccion :") #se guarda en comando columna

        columna = comando_columnas.split() #se divide en elementos de la lista 
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
                            print("Columna ya existe")
                        else:
                            tabla["Columnas"][columna[3]] = columna[4]
                            print(tabla)
                if(temp == False):
                    print("Tabla no encontrada")
            else: 
                print("Instruccion Incorrecta")
        else:
            print("Comando equivocado para agregar columna")


def Crear_tabla():

    
    comando_usuario = input("Digite su comando ");
    partes = comando_usuario.split();

    #print(partes[0]+' '+partes[1]);
    #print(comando_crear)
    #print(partes[-1]);   
    
    if(len(partes) == 3):
        comando_crear = partes[0]+' '+partes[1];
        if (comando_crear == "CREAR TABLA"):
            print("Tabla creada con exito!")

            nombre_tabla = {"Nombre":partes[2], "Columnas":{}} 
            """nombre_tabla = {"Nombre":partes[2],"ID_User_Paciente":int,"ID_DOC_Paciente":int,
                            "Nombres_Paciente":str,"Apellidos_Paciente ":str,
                            "Fecha_Nacimiento_Paciente":str,"Numero_Telefonico_Paciente":str,
                            "Correo_Electronico_Paciente":str,"Estado_Afiliacion":str} """
            #print(nombre_tabla)

            lista_tablas.append(nombre_tabla)
            print(lista_tablas)

            agregar_columna()
        else:
            print("Comando Incorrecto")
    else:
        print("Comando Incorrecto")




def modificar_tablas_columnas():
    #nothing here yet
    # MODIFICAR TABLA Nombre_Tabla Nuevo_Nombre (4)
    

    entrada = input("Digite la siguiente instruccion : ")
    comando = entrada.split();
    
    temp=''
    if (len(comando) == 4):
        if(comando[0] == "MODIFICAR"):
            if (comando[1]== "TABLA"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp= tabla
        
                if(temp != ''):
                    print("Elemento Encontrado")        
                    tabla["Nombre"] = comando[3] #aqui se cambia el nombre 
                    print(temp)
                else: 
                    print("Elemento No Encontrado")

            else:
                print("Comando Incorrecto")
        else:
            print("Comando Incorrecto")

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
                    print('Lista no encontrada')
                else:
                    for columna in temp_list["Columnas"]:
                        if(columna == comando[3]):
                            temp_col = columna

                if(temp_col == ''):
                    print("Columna no encontrada")
                else:
                    temp_list["Columnas"][comando[4]] = temp_list["Columnas"].pop(temp_col)
                    print(lista_tablas)


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
                    print('Lista no encontrada')
                else:
                    for columna in temp_list["Columnas"]:
                        if(columna == comando[3]):
                            temp_col = columna

                if (comando[4] == "TYPE"):
                    if(temp_col == ''):
                        print("Columna no encontrada")
                    else:
                        temp_list["Columnas"][temp_col] = comando[5]
                        print(lista_tablas)
                else:
                    print("Instruccion Incorrecta")

                     
def Eliminar_Tablas_Columnas():
    #ELIMINAR TABLA Nombre_Tabla 

    entrada = input("Digite la siguiente instruccion : ")
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

    #ELIMINAR COLUMNA Nombre_Tabla Nombre_Columna

    if(len(comando) == 4):

        if (comando[0] == "ELIMINAR"):
            if (comando[1] == "COLUMNA"):

                for tabla in lista_tablas:
                    if(tabla["Nombre"] == comando[2]):
                        temp_list = tabla

                if(temp_list == ''):
                    print(temp_list + '  Tabla no encontrada')
                else:
                    for columna in temp_list["Columnas"]:
                        if(columna == comando[3]):
                            temp_col = columna

                    if(temp_col == ''):
                        print( temp_col + " Columna no encontrada")
                    else: 
                        temp_list["Columnas"].pop(temp_col)
                        print(temp_col +" Columna eliminada satisfactoriamente")

        

            



        


                
            




#llamar a la funcion para crear una tabla 
Crear_tabla()
Crear_tabla()
modificar_tablas_columnas()
Eliminar_Tablas_Columnas()

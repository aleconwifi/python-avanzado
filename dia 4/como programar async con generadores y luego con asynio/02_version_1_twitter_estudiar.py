def twitter():
    print("t: leyendo a roberto")
    yield
    print('t: discutiendo con roberto')
    yield
    print('t: leyendo otras cosas')
    yield
    print('t: indignado por politica')

def estudiar():
    print('e: leyendo el material')
    yield
    print('e: armando resumen')
    yield
    print('e: leyendo el resumnen')
    print('e: memorizando resumen')
    yield
    print('e: llorando')


def loop(tareas):
    #mientras existan tareas pendientes
    while tareas:
        #sacar la primera,
        try:
            actual = tareas.pop(0)
            next(actual)

            #despues de sacarla tengo que agregarla a la lista de tareas pedientes, porque puede no terminarla. 
            #para que en algun momento se vuelva a ejecutar, la agrego al final de todo
            tareas.append(actual)
            # que pasa cuando una tarea de estas termine, manda un stopiteration, eso lo controlas con try
        except StopIteration:
            #dejarla pasar esa tarea termino
            pass


loop([twitter(), estudiar()])
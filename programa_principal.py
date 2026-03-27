peliculas = {}

nombre = input( ' Introduce un nombre o salir para terminar: ')

while nombre != 'salir':
    pelicula = input('Introduce la pelicula: ')
    puntaje = float (input(' Introduce el puntaje de la pelicula: '))
    
    if pelicula not in peliculas:
        peliculas[pelicula] = []
    
    peliculas[pelicula].append(puntaje)
    nombre = input( ' Introduce un nombre o salir para terminar: ')
    
mejor_n =''
mejor_p = -1

for pelicula  in peliculas:
    suma = 0
    for  p in peliculas[pelicula]:
        suma += p
    promedio = suma / len(peliculas[pelicula])
    print (pelicula, 'el promedio es', promedio)
    
    if promedio > mejor_p:
        mejor_p = promedio
        mejor_n = pelicula
        print(pelicula, 'es la pelicula recomendada')
        print('promedio', mejor_p)
    
    
    
    
        
        
    
        
    
    
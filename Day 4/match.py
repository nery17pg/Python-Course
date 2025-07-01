cliente = {'nombre': 'Nereyda', 
           'edad:': 20, 
           'ocupacion': 'estudiante'}

pelicula = {'titulo': 'Mulán',
            'ficha_tecnica': {'protagonista': 'Mulán',
                              'director': 'Tony Bancroft'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print("Es una película")
            print(titulo, protagonista, director)
        case _:
            print("No sé qué es esto")
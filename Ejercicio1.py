import time
import matplotlib.pyplot as plt

def two_sum_brute(arr):
    count = 0
    #TODO: Implementa la lógica de buscar todos los pares posibles
    # Tu código aquí:
    i=0 
    j= 0

    while i < len(arr):
        j = 0
        while j < len(arr):
            
            if arr[i] + arr[j] == 0:
                count += 1
            j += 1
        i += 1
    
    print(i, j)
    return count

# Pruebas y Tiempos de Ejecución empíricos
sizes = [100, 200, 400, 800, 1600]
times = []

for size in sizes:
    arr = list(range(-size//2, size//2))
    
    # Toma el tiempo antes de comenzar
    start_time = 0 # TODO: Reemplazar por método real
    
    two_sum_brute(arr)
    
    # Toma el tiempo al terminar
    end_time = 0 # TODO: Reemplazar por método real
    
    times.append(end_time - start_time)

# TODO: Escribe el código para mostrar el gráfico Lineal
def binary_search(input_list, item):
    # Inizializza i limiti inferiori e superiori
    low = 0
    high = len(input_list) - 1

    # Il ciclo continua finché ci sono elementi da esaminare
    while low <= high:
        # Calcola la posizione centrale
        mid = (low + high) // 2
        # Prendi l'elemento nella posizione centrale
        guess = input_list[mid]
        
        # Se l'elemento centrale è quello che cerchiamo, restituisci l'indice
        if guess == item:
            return mid
        
        # Se l'elemento centrale è più grande di quello cercato, riduci il limite superiore
        if guess > item:
            high = mid - 1
        else:
            # Altrimenti, aumenta il limite inferiore
            low = mid + 1
    
    # Se non trovi l'elemento, restituisci None
    return None
    

# Lista di prova
my_list = [1,3,5,7,9,11,13,15,17,19,21,23,25]

# Stampa la posizione dell'elemento 3 (che si trova nella posizione 1)
print(binary_search(my_list, 3))  # Deve restituire posizione 1

# Stampa la posizione dell'elemento 23 (che si trova nella posizione 11)
print(binary_search(my_list, 23)) # Deve restituire posizione 1

# Cerca un elemento che non è nella lista, restituisce None
print(binary_search(my_list, -1)) # None, questo numero non è presente nella lista

            
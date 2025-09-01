  # 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
  # de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
  # modo: 

peso=float(input("ingresa tu peso en kg: "))
altura=float(input("ingresa tu altura en metros: "))
indice_corporal=peso/(altura*altura)
print(f"Tu indice corporal es: {indice_corporal}")

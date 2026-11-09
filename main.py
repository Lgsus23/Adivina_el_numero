import random

max_number = 10

def guess():
    
    print (f'Piensa un número del 0 al {max_number}')
    Numbers_called= []
    
    while len(Numbers_called) < max_number + 1:
        random_guess = random.randint(0, max_number)

        if random_guess in Numbers_called:
            continue

        Numbers_called.append(random_guess)
        election= input(f"¿El número {random_guess} es el correcto? si / no: ").lower()

        if election == "si":
            print(f"me tomó { len(Numbers_called) } intentos pero igual la pegué")
            break
        print("Intento de nuevo")
    else: 
        print("¿estás seguro que no te lo adiviné?")
   
guess()
pessoas = input("Quantidade de pessoas:") # Recebe o número de pessoas
tipodereuniao = input("Tipo de reunião:") # Recebe o tipo de reunião

intpessoas = int (pessoas) # Converte a variável pessoas para inteiro
strtipodereuniao = str (tipodereuniao) # Converte a variável tipodereuniao em streing

if intpessoas <= 5: # Para reunião até 5 pessoas
    print ("Sala pequena para a reunião", strtipodereuniao,"com", intpessoas, "pessoas.")

elif intpessoas <= 15: # Para reunião até 15 pessoas
    print ("Sala média para a reunião", strtipodereuniao,"com", intpessoas, "pessoas.")

else: # 16 pessoas ou mais.
    print ("Sala grande para a reunião", strtipodereuniao,"com", intpessoas, "pessoas.")
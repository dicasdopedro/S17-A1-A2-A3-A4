funcionario = input("Digite o cargo:")

if funcionario == 'gerente':
    print("Entra a qualquer hora.")

elif funcionario == 'analista':
    print("Entra fora do horário com autorização do gerente.")

elif funcionario == 'estagiário':
    print("2ª a 6ª")

else:
    print("Este cargo não existe aqui.")
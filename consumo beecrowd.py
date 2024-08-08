km = input ("Quantos kilômetros percorridos?") # recebe
combustivel = input("Quantos litros gastou?")

kmrodado = int (km) # faz conversão
combustivelgasto = float (combustivel)

consumomedio = kmrodado / combustivelgasto # calcula os dados convertidos

cma = round (consumomedio, 3) # Consumo Médio Arredondado para 3 casas após a virgula

print ("Total de ", cma, " litros por km!") # Resultado
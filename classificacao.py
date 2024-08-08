classificacao = input("Digite a classificação desejada:")

"""
Classificação para assistir filme.
"""

if classificacao == "CA": # A variável recebeu um dado digitado
    mensagem = "Apropriado para todas as idades." # A variável mensagem recebe o if. 

elif classificacao == "AE":
    mensagem = "Crianças menores de idade devem estar acompanhadas."

elif classificacao == "AO":
    mensagem = "Apenas para maiores de 18 anos."

else:
    mensagem = "Classificação desconhecida."

print(mensagem) # Será exibida a mensagem de acordo com a condição.
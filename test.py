from numpy import array

#Pergunta quantos saltos foram realizados
quant = int(input("Quantos saltos foram realizados: "))

#Insere os saltos no vetor dist

dist =[]
entrada = 0
for i in range(quant):
    entrada = float(input(f'distancia do salto {i+1} : '))
    dist.append(entrada)


#Procura Maior e Menor Valor
maxSalto = round(max(dist),2)
minSalto = round((len(dist)-1),2)

#Saidas
print('maior distância: ',maxSalto)
print('Outros Saltos: ',minSalto)

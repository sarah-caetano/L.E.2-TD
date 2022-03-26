msg = "HGBRR"
result = ""
cont = 0
for char in msg:
    if not result:
        print("not result")
        result += char
        cont += 1
        print("result = " + result)

    elif(result[-1] == char): # compara se o char atual é igual ao último char da string
        print("comparacao = result(" + result[-1] + ") char (" + char + ")")
        cont+=1 #conta quantas vezes aquele caractere apareceu
        print("cont = " + str(cont))

    else:
        print("caractere n igual")
        result += str(cont) #coloca as repetições dentro da string
        result += char # coloca o novo char na string
        cont = 1 # restaura o valor do contador pro novo char
        print("result = " + result)

result += str(cont) #coloca a última ocorrência 
print(result)


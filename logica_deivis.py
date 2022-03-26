senha = "AbcdEfgh99"
maiuscula = 0
minuscula = 0
tam_err = 0
numero = 0
nao_char = 0

if (len(senha) < 6 or len(senha) > 32): # verifica tam
    print("Tam invalido")
    tam_err +=1

else: # verifica as letras
    for char in senha:
        print(char)
        if (char >= 'A' and char <= 'Z'):
            print("Existe maiuscula")
            maiuscula +=1
        elif (char >= 'a' and char <= 'z'):
            print("Existe minuscula")
            minuscula +=1
        elif (char >= '0' and char <= '9'):
            print("Existe numero")
            numero +=1
        else:
            print("nao caractere")
            nao_char +=1
            break

if(tam_err > 0 or maiuscula == 0 or minuscula == 0 or numero == 0 or nao_char > 0):
    print("tam_err = ", tam_err, " maiuscula = " , maiuscula , " minuscula = " , minuscula , " nao_char = " , nao_char)
    print("Senha inválida!")

else: print("Senha valida.")


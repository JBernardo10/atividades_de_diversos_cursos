try:
    #operacao
    a = int(input("numerador: "))
    b = int(input("denominador: "))
    r = a /b
except (ValueError, TypeError):
    #erro de tipo dos dados
    print("tivemos um problema com os tipos de dados que vc digitou")
except ZeroDivisionError:
    #divisão por zero
    print("nao é possivel dividir por zero")
except KeyboardInterrupt:
    #interromper o programa
    print("o usuario preferiu nao informar os dados")
except Exception as erro:
    #falha
    #print("erro, tivemos um problema :(")
    print(f"o problema encontrado foi {erro}")
else:
    #deu certo
    print(f"o resultado e {r}")

finally:
    #certo/falha
    print("volte sempre, muito obrigado")





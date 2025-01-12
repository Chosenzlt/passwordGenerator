import random
import string

def gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_simbulos);
    caracteres = string.ascii_lowercase

    if incluir_maiusculas;
        caracteres += string.ascii_uppercase
    if incluir_numeros;
        caracteres += string.digits
    if incluir_simbulos;
        caracteres += string.punctuation

senha = join(random.choice(caracteres) for _ in range(tamanho))
return(senha)

# Programa principal
if _name_ == "__main__";
   print("Bem-vindo ao Gerador de Senhas Aleatórias")

#Entrada do usuario   
   tamanho = int(input("Digite o Tamnho da Senha"))
   incluir_maiusculas = input("Incluir letras maiusculas? (s/n):").lower() == 's'
   incluir_numeros = input("Incluir numeros? (s/n):").lower() == 's'
   incluir_simbulos = input("Incluir simbulos? (s/n):").lower() == 's'

#Gerar senha
senha_gerada = gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_simbulos)
print(f"sua senha gerada é {senha_gerada}")

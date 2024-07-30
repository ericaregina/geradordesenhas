import random
import string

def gerar_senha(comprimento=12, incluir_simbolos=True):
    caracteres = string.ascii_letters + string.digits  # Letras e dígitos
    if incluir_simbolos:
        caracteres += string.punctuation  # Adiciona símbolos especiais
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

comprimento_desejado = 16
senha = gerar_senha(comprimento=comprimento_desejado, incluir_simbolos=True)
print(f"Sua senha gerada é: {senha}")

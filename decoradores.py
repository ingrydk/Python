def meu_decorador(funcao):
    def envelope(*args,**kwargs):
        print("faz algo antes de executar")
        funcao(*args,**kwargs)
        print("faz algo antes de executar")
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f'ola mundo {nome}!')

#assim nao é mais necessário a forma abaixo
#ola_mundo=meu_decorador(ola_mundo)

ola_mundo("Joao",1996)
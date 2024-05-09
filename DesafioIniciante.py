capacidade_atual, aumento_percentual = map(int, input().split())

# Calcule a nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual+((aumento_percentual/100)*capacidade_atual)

# Imprima a nova capacidade
print(round(nova_capacidade))
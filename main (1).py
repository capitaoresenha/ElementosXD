sigla = input("Digite a sigla dos seguintes elementos (Sn, Sr, Fm, Ba, C, Cu, S, F, Fe, O) para informações aprofundadas: ").capitalize()

tabela = {
 'Sn': {'nome': 'Estanho', 'valor_de_massa': '118,69', 'numero_atomico': '50'},
'Sr': {'nome': 'Estrôncio', 'valor_de_massa': '87.62', 'numero_atomico': '38'},
'Fm': {'nome': 'Férmio', 'valor_de_massa': '(257)', 'numero_atomico': '100'},
'Ba': {'nome': 'Bário', 'valor_de_massa': '137.327', 'numero_atomico': '38'},
'C': {'nome': 'Carbono', 'valor_de_massa': '12.011', 'numero_atomico': '6'},
'Cu': {'nome': 'Cobre', 'valor_de_massa': '63.546', 'numero_atomico': '29'},
'S': {'nome': 'Enxofre', 'valor_de_massa': '32.065', 'numero_atomico': '16'},
'F': {'nome': 'Flúor', 'valor_de_massa': '18.998', 'numero_atomico': '9'},
'Fe': {'nome': 'Ferro', 'valor_de_massa': '55.845', 'numero_atomico': '26'},
'O': {'nome': 'Oxigênio', 'valor_de_massa': '15.999', 'numero_atomico': '8'},
    
    
} 

if sigla in tabela:
  print(f'O nome do seu elemento é: {tabela[sigla]["nome"]}')
  print(f'O valor de massa do seu elemento é: {tabela[sigla]["valor_de_massa"]}')
  print(f'O número atômico do seu elemento é: {tabela[sigla]["numero_atomico"]}')
else:
    print('Sigla de elemento indisponível ou inválida, tente novamente.')





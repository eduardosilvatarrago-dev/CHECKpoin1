import random
tentativa = 0
numero_secreto = random.randint(1, 100)
escolha = 0 
while escolha != numero_secreto:
  if tentativa >= 7:
    print(f'tentativas esgotadas.')
    break
  try:
    escolha = int(input('tente adivinhar o numero: '))
    tentativa += 1 

    if escolha == numero_secreto:
      print(f'Parabéns, você acertou em {tentativa} tentativas!')
    elif escolha < numero_secreto:
      print('Tente um número maior.')
    else: 
      print('Tente um número menor.')
  except ValueError:
    print('Entrada inválida. Por favor, digite um número inteiro.')

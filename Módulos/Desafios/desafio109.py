num = float(input('Digite o preço do seu produto: R$ '))
import modulo1
print(f'Seu produto vale {modulo1.dinheiro(num)}\n'
      f'O dobro dele é {modulo1.dobro(num, True)}\n'
      f'A metade é {modulo1.metade(num, True)}\n'
      f'Com 10% a mais é {modulo1.aumentar(num, 0.1, True)}\n'
      f'Reduzindo 13%, temos {modulo1.diminuir(num, 0.13, True)}')

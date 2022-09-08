num = float(input('Digite o preço do seu produto: R$ '))
import modulo1
print(f'Seu produto vale {modulo1.dinheiro(num)}\n'
      f'O dobro dele é {modulo1.dinheiro(modulo1.dobro(num))}\n'
      f'A metade é {modulo1.dinheiro(modulo1.metade(num))}\n'
      f'Com 10% a mais é {modulo1.dinheiro(modulo1.aumentar(num, 0.1))}')


# Criação e Utilização de módulos. Para ver código do módulo acesse a pasta Módulos
import modulo1
num = float(input('Digite o preço do seu produto: R$ '))

print(f'Seu produto vale R${num}\n'
      f'O dobro dele é R${modulo1.dobro(num)}\n'
      f'A metade é R${modulo1.metade(num)}\n'
      f'Com 10% a mais é R${modulo1.aumentar(num, 0.1)}')


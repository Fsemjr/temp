def menu_Inicial():
  print('Programa para conversão de Temperatura')
  print('1. - Converter Celcius para Fahrenthi')
  print('2. - Converter Fahrenthi para Celcius ')

  def cel_far():
    C = float(input('Insira a Temperatura em Celsius '))
    F = C * ( 9 / 2 ) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))


    def fahr_cel():
      F = float(input('Entre com a temperatura em graus Fahrenheit: '))
      C = (F - 32) * (5 / 9)
      print('Valor em Celsius: {0}°C'.format(C))

      if __name__=='__main__':
        menu_inicial()
        escolha = input('Escolha o tipo de conversão que deseja realizar: ')

      if escolha == '1':
        cel_fahr()

      if escolha == '2':
        fahr_cel()
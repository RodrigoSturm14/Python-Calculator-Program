suma = 1
resta = 2
multiplicacion = 3
division = 4

end_while = False
last_answer = 0

def in_operation():
  return input(''' Calculadora
      1- Suma
      2- Resta
      3- Multiplicacion
      4- Division
Indicar operacion a realizar: ''')

def op_sum():
  print()
  print('             SUMA')
  print('- Ingrese dos numeros para sumar:')
  input1 = input('Primer numero: ')
  num1 = int(input1) if input1 != 'ans' else last_answer

  input2 = input('Segundo numero: ')
  num2 = int(input2) if input2 != 'ans' else last_answer

  resultado = num1 + num2
  print(f'{num1} + {num2} = {resultado}')
  return resultado

def op_subtraction():
  print()
  print('             RESTA')
  print('- Ingrese dos numeros para restar:')
  input1 = input('Primer numero: ')
  num1 = int(input1) if input1 != 'ans' else last_answer

  input2 = input('Segundo numero: ')
  num2 = int(input2) if input2 != 'ans' else last_answer

  resultado = num1 - num2
  print(f'{num1} - {num2} = {resultado}')
  return resultado

def op_mult():
  print()
  print('           MULTIPLICACION')
  print('- Ingrese dos numeros para sumar:')
  input1 = input('Primer numero: ')
  num1 = int(input1) if input1 != 'ans' else last_answer

  input2 = input('Segundo numero: ')
  num2 = int(input2) if input2 != 'ans' else last_answer

  resultado = num1 * num2
  print(f'{num1} * {num2} = {resultado}')
  return resultado

def op_div():
  print()
  print('             DIVISION')
  print('- Ingrese dos numeros para sumar:')
  input1 = input('Primer numero: ')
  num1 = int(input1) if input1 != 'ans' else last_answer

  input2 = input('Segundo numero: ')
  num2 = int(input2) if input2 != 'ans' else last_answer

  resultado = num1 / num2
  print(f'{num1} / {num2} = {resultado}')
  return resultado

def while_state():
  answer = ''
  while answer != 'N' or 'n' or 'S' or 's':
    state = input('¿Continuar operando? (S/N) ')
    if state == 'N' or state == 'n' :
      end_while = True
      return end_while
    elif state == 'S' or state == 's' :
      end_while = False
      return end_while

while end_while == False:
  var_operacion = in_operation()
  match var_operacion:
    case '1':
      last_answer = op_sum()
      end_while = while_state()
      print(end_while)
    
    case '2':
      last_answer = op_subtraction()
      end_while = while_state()

    case '3':
      last_answer = op_mult()
      end_while = while_state()

    case '4':
      last_answer = op_div()
      end_while = while_state()

    case _:
      print('Opcion invalida')
      end_while = False
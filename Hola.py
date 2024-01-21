resultado = 2+2;

mensaje = f"2+2 es = {resultado}";
print(mensaje);
var_pertenencia = "4" not in mensaje;
print(var_pertenencia);


array_datos_personales = ['Rodrigo', 'Sturm', 17, ['Argentina', 'Buenos Aires']];

print(f'Nombre: {array_datos_personales[0]}');
print(f'Lugar de nacimiento: {array_datos_personales[3][0]}, {array_datos_personales[3][1]}');

array_datos_personales[0] = 'Rodrigo Hector';

print(f'Nombre: {array_datos_personales[0]}');

float_var = 190.1;

print(f'Altura: {float_var}');

football_fan = True;

if(football_fan == True):
  print('Hincha de Racing C.');
else:
  print('Hincha de Inter de Milan');

deporte = '45'

print(deporte.replace('a', 'ñ'))

print(int(deporte))
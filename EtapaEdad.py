edad = int(input('proporciona tu edad: '))
etapa = None

if edad == 0 or edad < 10:
    etapa = 'la infacncia es increible...'
elif edad == 10 or edad < 20:
    etapa = 'Muchos cambios y mucho estudio...'
elif edad == 20 or edad <= 30:
    etapa = 'Amor y comienza el trabajo...'
else:
    etapa = 'Etapa de vida no reconocidad'
print(etapa)
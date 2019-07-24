segundos = input("Por favor, entre com o número de segundo que deseja converter: ")
segundosInteiro = int(segundos)

dia = segundosInteiro // 86400
hora = ((segundosInteiro // 3600) % dia)
segundosRestante = segundosInteiro % 3600
minuto = segundosRestante // 60
segundosFinal = segundosRestante % 60

print (dia,"dias,",hora,"horas,",minuto,"minutos e",segundosFinal,"segundos.")

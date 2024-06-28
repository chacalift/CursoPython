dados = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos_total = int(dados)


dias = segundos_total // 86400
segundos_restantes = segundos_total % 86400
horas = segundos_restantes // 3600
segundos_restantes %= 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60


print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")

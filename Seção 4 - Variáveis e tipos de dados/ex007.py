""" Leia uma velocidade em km/h e apresente-a convertida em m/s."""
print('Conversor de Velocidade\nKm/h --> m/s')
kmh = float(input('Qual a velocidade em Km/h: '))
ms = kmh / 3.6
print(f'A velocidade de {kmh}km/h é igual a {ms:.2f}m/s')

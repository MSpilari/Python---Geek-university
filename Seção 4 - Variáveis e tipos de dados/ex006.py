""" Leia uma temperatura em °C e apresente-a convertida em °F"""
temperatura = float(input('Informe a temperatura em °C: '))
conversor = temperatura * (9/5) + 32
print(f'A temperatura {temperatura}°C em em Fahrenheit é {conversor}°F')

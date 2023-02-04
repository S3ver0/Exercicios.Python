## Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
## Considera US$1,00=RS$3,37.
real = float(input('Quando dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print ('Com RS{:.2f} você pode comprar US${:.2f}'.format(real, dolar))

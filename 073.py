times = ('Internacional', 'Flamengo', 'Atletico-MG', 'Fluminense', 'Sao Paulo', 'Santos', 'Palmeiras', 'Gremio',
         'Sport Recife', 'Fortaleza', 'Corinthians', 'Ceara SC', 'Atletico-GO', 'Botafogo', 'Bahia', 'Vasco da Gama',
         'Coritiba', 'Bragantino-SP', 'Atletico-PR', 'Goias')

print(f'Lista de times do Brasileirão: {times}')
print('-'*30)
print(f'Os 5 primeiros são: {times[:5]}')
print('-'*30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-'*30)
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O Palmeiras está na {times.index("Palmeiras")+1}ª posição')
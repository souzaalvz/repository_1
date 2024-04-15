velocidade = 10  # m/s
velocidade_kmh = velocidade * 3.6
 
periodo_semanas = 1
periodo_segundos = periodo_semanas * 7 * 24 * 60 * 60
 
distancia_km = velocidade_kmh * (periodo_segundos / 3600)
print("A ave percorreu uma distância de", distancia_km, "quilômetros durante uma semana.")
import geopy.distance as gd
import requests
import json

def buscar_distancias(endereco_usuario, enderecos_banco):
    resultados = []
    
    url_geocode = f'https://nominatim.openstreetmap.org/search?q={endereco_usuario}&format=json'
    response_geocode = requests.get(url_geocode)
    dados_geocode = json.loads(response_geocode.content)
    
    coordenadas_usuario = (float(dados_geocode[0]['lat']), float(dados_geocode[0]['lon']))
    
    for endereco in enderecos_banco:
        url_geocode = f'https://nominatim.openstreetmap.org/search?q={endereco}&format=json'
        response_geocode = requests.get(url_geocode)
        dados_geocode = json.loads(response_geocode.content)
        
        coordenadas_endereco = (float(dados_geocode[0]['lat']), float(dados_geocode[0]['lon']))
        
        distancia = round(gd.distance(coordenadas_usuario, coordenadas_endereco).km, 2)
        
        resultados.append(f'{endereco}: {distancia} km')
    

    return resultados
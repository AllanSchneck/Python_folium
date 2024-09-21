import requests
#MAPAS EM PYTHON
import math;
import folium;
from folium import plugins;
#folium é uma biblioteca para mapas
sete_maravilhas_nomes = ["Grande Pirâmide de Gizé, no Egito",
"Jardins Suspensos da Babilônia",
"Templo de Ártemis, em Éfeso",
"Estátua de Zeus, em Olímpia",
"Mausoléu de Halicarnasso",
"Colosso de Rodes",
"Farol de Alexandria"]
print(sete_maravilhas_nomes)
sete_maravilhas_coordenadas = [
[29.979, 31.134],[32.544, 44.420],
[37.949, 27.363],[37.637, 21.630],
[37.037, 27.424],[36.451, 28.227],
[31.214, 29.891]]
mapas = folium.Map(
                location=[31.214, 29.891],#localizacao
                zoom_start=5,#comeca o zoom
                control_scale=True,# controlador de scala ede zoom
                tiles="cartodbpositron"#mapa inicial
                   )
#digitando o nome do layer para o mapa comecar ou ficar definitivo
folium.TileLayer("cartodbpositron").add_to(mapas)#criando uma camada do mapa 
#Stamen Toner
folium.TileLayer(tiles= 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                 attr= 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
                 name= 'Thunderforest.OpenCycleMap' ).add_to(mapas)#cria uma camada de mapa com cores
folium.LayerControl().add_to(mapas) #permite outros layers de mapa
#precisamos preencher estes atributos para replicar as config de mapas que estao amostra neste link 
#https://leaflet-extras.github.io/leaflet-providers/preview/
print(len(sete_maravilhas_coordenadas))
for i in range(len(sete_maravilhas_coordenadas)):#conta até sete range da setemaravilhas com 7 itens
    cordenada = sete_maravilhas_coordenadas[i] #adiciona cordenada conforme "i"(contador) e exclui ultima
    maravilha = sete_maravilhas_nomes[i] #adiciona maravilha conforme "i"(contador) e exclui ultima
    folium.Marker(cordenada,#variavel cordenada para ser marcada
                  popup=maravilha,#nome da maravilha em popup
                  tooltip="Veja",
                  icon=folium.Icon(#ICONE CRIAÇÃO
                        icon="glyphicon glyphicon-picture",#nomedoicone em bootstrap
                        color="black",#cor de fundo
                        icon_color="white",#cor do icone
                        prefix='glyphicon')).add_to(mapas)#prefix serve para dizer que é associado a bootstra e Glyphicons
    #https://getbootstrap.com/docs/3.3/components/
mapas.add_child(folium.LatLngPopup())#criar um popup com coordenadas ao click
mapas.save("index.html")#salve em documento html    



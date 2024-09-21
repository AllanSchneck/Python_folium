##Criando um mapa com localização em tempo real em python
#com folium
import folium;
import folium.features
from folium.plugins import LocateControl;
mapa = folium.Map(location=[31.12,22.21],zoom_start=5)
folium.TileLayer(tiles= 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                 attr= 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
                 name= 'Thunderforest.OpenCycleMap').add_to(mapa)
folium.LayerControl().add_to(mapa)
folium.Marker(location=[29.123,32.123],popup="aprede ai nerd",tooltip="olha aqui").add_to(mapa)
folium.Marker(location=[30.721, 23.0360],popup="Email",tooltip="Clique e saiba mais",icon=folium.Icon(icon="cloud")).add_to(mapa)   
folium.Marker(
    location=[23.813, 29.847],popup="A receber",tooltip="Clique e saiba mais",icon=folium.Icon(icon="envelope",
    color="red")).add_to(mapa)
variavel_folium_location= [32.776, 11.434]
variavel_folium_popup= "<strong>ICONE PERSONALIZADO<strong><br>Este é um exemplo de popup personalizado<br>"    

variavel_folium_icone1 = folium.features.CustomIcon(icon_image=".idea/inspectionProfiles/imagens/icone1.jpeg", icon_size=0.1)
folium.Marker(location=variavel_folium_location,popup=variavel_folium_popup,tooltip="Clique e veja",icon=variavel_folium_icone1).add_to(mapa)

folium.LatLngPopup().add_to(mapa)
LocateControl(auto_start=True,  # auto_Start serve para que logo que o arquivo comecar ja pegar os dados de localização do usuario
   keepCurrentZoomLevel =True, #  keepCurrentZoomLevel possibilita um corrigir problemas com zoom comecando com o mesmo zoom_start de #antes
              drawMarker=True, #drawMarker serve para desenhar um marcador
              markerStyle = dict(ClassName = "leaflet-control",color="orange", #criaum estilo de marcador com classe do dicionario "leaflet-control",cor laranja do ponto
                               fillColor="black", #borda do ponto
                               fillOpacity=2,#opacidade do fill
                               opacity=100,#opacidade do ponto
                               weight=1,#tamanho
                               radius=1),#raio
                               drawCricle= True,#Criando circulo de range ao redor do ponto
                               circleStyle = dict(ClassName="leaflet-control-locate-circle",#nome do dicionario de circle
                                                  weight=1, #tamanho
                                                  color="red",#cor da borda
                                                  opacity =21),#opacidade
                                                  drawString=True,
                                                  string = dict(title= "onde estou!",#
                                                               popup="aqui")).add_to(mapa)#

mapa.save("lcl_atual.html")
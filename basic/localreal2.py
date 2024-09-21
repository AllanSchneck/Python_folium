import folium;#importa biblioteca folium
from folium.plugins import LocateControl;#Importa LocateControl da biblioteca folium
mapa = folium.Map([21.12,32.21],zoom_start=5,tiles="cartodbpositron",control_scale=True)
#cria variavel "mapa" da classe folium.folium.Map com cooredenadas do inicial do mapa (zoom_start)=comeca #o zoom,tiles="cartodbpositron"=começa neste layer de "mapa"
folium.TileLayer(tiles="cartodbpositron").add_to(mapa)#adiciona este layer ao "mapa"

LocateControl(auto_Start=True,
              keepCurrentZoomLevel =False, 
              drawMarker=True).add_to(mapa) #LocateControl serve para localização em tempo real 
# auto_Start serve para que logo que o arquivo comecar ja pegar os dados de localização do usuario
#  keepCurrentZoomLevel possibilita um corrigir problemas com zoom comecando com o mesmo zoom_start de #antes
#drawMarker serve para futuramente desenhar um marcador


mapa.save("local.html")#salvando em arquivo html

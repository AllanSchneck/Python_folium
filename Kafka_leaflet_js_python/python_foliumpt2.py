#Python com geojson folium e leaflet
import base64
from folium import IFrame
import folium
import os
mapa = folium.Map(location=[52.1603, 7.4983],
                  zoom_start=15)
Walkdado = os.path.join('.idea/inspectionProfiles/caminhada.json')
caminho = folium.GeoJson(Walkdado)
caminho.add_to(mapa)
tooltip1 = "click to see picuture"
html = '<img src="data:image/png;base64,{}">'.format
folium.LayerControl().add_to(mapa)
folium.LatLngPopup().add_to(mapa)
picuture1 = base64.b64encode(open('.idea/inspectionProfiles/imagens/pepe.png', 'rb').read()).decode()
iframe1 = IFrame(html(picuture1, 
                width=400,
                height=200))
popup1 = folium.Popup(iframe1,
                      max_width=1050)
marker1 = folium.Marker(location=[52.1589,7.4959],
                        popup=popup1,
                        tooltip=tooltip1,
                        icon = folium.Icon(icon='glyphicon glyphicon-file',
                                           color="red",
                                           prefix='glyphicon'
                                            )).add_to(mapa)
#-----------------
picuture2 = base64.b64encode(open('.idea/inspectionProfiles/imagens/dodge.jpeg', 'rb').read()).decode()
#base64
# Base64 é uma técnica de codificação que permite representar dados binários (como imagens ou #     arquivos) em uma string de texto usando apenas caracteres alfanuméricos e alguns sinais de adição 
# (+, /). Isso é útil para transmitir dados em formatos que não suportam binários diretamente, como # e-mails ou URLs.
#Em Python, você pode usar a biblioteca padrão base64 para codificar e decodificar dados em Base64. Aqui está um exemplo simples:
# b64encode(): Codifica dados binários em Base64.
# b64decode(): Decodifica dados em Base64 de volta ao formato original
iframe2 = IFrame(html(picuture2,
                      width=500,
                      height=200))
popup2= folium.Popup(iframe2,
                     max_width=700)
marker2= folium.Marker(location=[52.1594, 7.5056],
                       popup=popup2,
                       tooltip=tooltip1,
                       icon= folium.Icon(
                           icon='glyphicon glyphicon-file',
                           color="blue",
                           prefix='glyphicon'
                       )).add_to(mapa)
picuture3 = base64.b64encode(open('.idea/inspectionProfiles/imagens/mo paz.jpeg','rb').read()).decode()
iframe3= IFrame(html(picuture3,
                     height=200,
                     width=400))
popup3= folium.Popup(iframe3,
                     max_width=100)
marker3= folium.Marker(location=[52.1622, 7.4978],
                       popup=popup3,
                       tooltip=tooltip1,
                       icon= folium.Icon(
                           icon='glyphicon glyphicon-file',
                           color='green',
                           prefix='glyphicon'
                       )).add_to(mapa)
mapa.save('geo.html')

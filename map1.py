import folium
import pandas

def get_color(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

data = pandas.read_csv("Volcanoes.txt")
lat = list(data.LAT)
lon = list(data.LON)
elv = list(data.ELEV)
map = folium.Map(location=[38.53,-99.09],zoom_start=6,tiles="MapBox Bright")

fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat,lon,elv):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=7, popup= str(el)+" m",fill_color=get_color(el),color = 'black',fill_opacity =0.7))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")

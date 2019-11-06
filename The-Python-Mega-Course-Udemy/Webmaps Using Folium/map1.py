import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location = [28.6139, 77.2090], zoom_start = 3, tiles = "Mapbox Bright")

def colCheck(elevation):
    if elevation < 1000:
        return 'green'
    elif (1000 <= elevation < 3000):
        return 'orange'
    else :
        return 'red'

fgv = folium.FeatureGroup(name = "Volcanoes")

for i, j, k in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [i, j], radius = 6, popup = str(k) + " m", fill_color = colCheck(k), color = 'grey'
    , fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")

fgv.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig'), style_function = lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

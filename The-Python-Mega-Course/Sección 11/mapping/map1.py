import folium
import pandas

#This map contains base layer, marker layer and polygon layer

map       = folium.Map(location      =[19.72,-103.46], zoom_start =4, tiles ="Mapbox Bright")
volcanoes = pandas.read_csv("Volcanoes.txt")
lat       = list(volcanoes["LAT"])
lon       = list(volcanoes["LON"])
elev      = list(volcanoes["ELEV"])

def elevColor (x):
    if x<1000          :
        return "green"
    elif 1000<= x <3000:
        return "orange"
    elif x>3000        :
        return "Red"

#Adding a marker from a FeatureGroup
fg        = folium.FeatureGroup(name ="Population")
fgcm      = folium.FeatureGroup(name="Volcano Markers")
#Iterating two lists
for lt, ln, elv in zip(lat, lon, elev):
    fgcm.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(elv)+" mts" ,
                 fill=True, color="grey", fill_color=elevColor(elv), fill_opacity=1))

#Adding polygons and filling them with a certain color depending the country population
fg.add_child(folium.GeoJson(data=open("world.json","r", encoding="utf-8-sig").read(),
             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 25000000
             else 'orange' if 25000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))


'''
NOTE You may get a blanck web page if there are quotes (') in the strings. To avoid
that change the popup argument to: popup=folium.Popup(str(elv), parse_html=true)


Adding a layer control. This control is in Folium library. We have to add This
control once we've added all the layers
'''

map.add_child(fg)
map.add_child(fgcm)

map.add_child(folium.LayerControl())

#Adding a Marker
#map.add_child(folium.Marker(location=[18.72,-103.46], popup="Hi I am a Marker", icon = folium.Icon(color='green')))

map.save("Map1.html")

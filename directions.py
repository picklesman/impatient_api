#!/usr/bin/env python
from googlemaps import GoogleMaps

def time_from_coords(src_coords, dst_coords):
    gmaps = GoogleMaps()
    src_addr = gmaps.latlng_to_address(*src_coords).encode('utf-8')
    dst_addr = gmaps.latlng_to_address(*dst_coords).encode('utf-8')
    
    dirs = gmaps.directions(src_addr,dst_addr)
    
    #returns - distance km, time min
    dist = dirs.get('Directions',{}).get('Distance',{}).get('html','')
    duration =  dirs.get('Directions',{}).get('Duration',{}).get('html','')
    
    return (dist,duration)



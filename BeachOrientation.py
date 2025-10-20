"""
Beach facing direction calculator
---------------------------------
Given two endpoints of a beach (lat/lon), this script calculates the 
perpendicular direction (the "facing" direction, i.e., toward the sea).

Run:
    python beach_facing.py
"""

import math

def normalize(deg):
    return (deg + 360) % 360

# def bearing(lat1, lon1, lat2, lon2):
#     """Initial bearing from point A to B."""
#     lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
#     dlon = lon2 - lon1
#     x = math.sin(dlon) * math.cos(lat2)
#     y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
#     brng = math.degrees(math.atan2(x, y))
#     return normalize(brng)

# def compass_label(bearing):
#     """Return nearest 16-wind compass label."""
#     dirs = [
#         "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
#         "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW",
#     ]
#     return dirs[int((bearing + 11.25) // 22.5) % 16]

# def beach_facing(lat1, lon1, lat2, lon2, sea_side="right"):
#     """
#     Compute the facing direction (perpendicular to the shoreline).

#     sea_side: "left" or "right" (when moving from point A→B)
#     """
#     alongshore = bearing(lat1, lon1, lat2, lon2)
#     if sea_side.lower() == "right":
#         facing = normalize(alongshore + 90)
#     else:
#         facing = normalize(alongshore - 90)
#     return facing, compass_label(facing)

def beach_facing(lat1, lon1, lat2, lon2):
    """
    compute the bearing spanning the shoreline from point 1 to point 2"""

    deltalat = lat2 - lat1
    deltalon = lon2 - lon1
    bearing_rad = math.atan2(deltalon, deltalat)
    bearing_deg = math.degrees(bearing_rad)
    bearing_deg = normalize(bearing_deg)
    return bearing_deg

if __name__ == "__main__":
    print("Enter coordinates for the two beach endpoints:")
    lat1 = float(input("Latitude 1: "))
    lon1 = float(input("Longitude 1: "))
    lat2 = float(input("Latitude 2: "))
    lon2 = float(input("Longitude 2: "))
    beach_span = beach_facing(lat1, lon1, lat2, lon2)
    print(f"Beach shoreline bearing from point 1 to point 2: {beach_span:.2f}°")
    # sea_side = input("Is the sea to the 'left' or 'right' when going from point 1 to 2? [right]: ") or "right"
    facing_direction = beach_span + 90  # assuming sea is to the right
    facing_direction = normalize(facing_direction)
    print(f"Beach facing direction (toward the sea): {facing_direction:.2f}°")

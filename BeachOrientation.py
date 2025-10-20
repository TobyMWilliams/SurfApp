"""
Beach facing direction calculator
---------------------------------
Given two endpoints of a beach (lat/lon), this file calculates the 
perpendicular direction (the "facing" direction, i.e., toward the sea).


"""

import math

# method to normalize degrees to [0, 360)
def normalize(deg):
    return (deg + 360) % 360

# method to compute bearing between two lat/lon points
# using simple planar approximation
def beach_facing(lat1, lon1, lat2, lon2):
    """
    compute the bearing spanning the shoreline from point 1 to point 2"""

    deltalat = lat2 - lat1
    deltalon = lon2 - lon1
    bearing_rad = math.atan2(deltalon, deltalat)
    bearing_deg = math.degrees(bearing_rad)
    bearing_deg = normalize(bearing_deg)
    return bearing_deg

# Example usage
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

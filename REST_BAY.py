# TODO this file should be replaced by a proper database or config file
# for now, we just hardcode the values for Rest Bay

# this file is used to store the constant values for Rest Bay(Porthcawl)
    # latitude and longitude coordinates
    # Rest Bay Beach Coordinates

REST_BAY_COORDINATES = {
    "name": "Rest Bay",
    "cardinal_facing": "WSW",
    "facing": 220.67, # degrees
    "TL_latitude": 51.493065818283526,
    "TL_longitude": -3.7369254726417918,
    "BR_latitude": 51.48506061928513,
    "BR_longitude": -3.7276070910297494,
}

# Preferable conditions for surfing at Rest Bay:
    # - Optimal Tide: Mid to High Tide
    # - Best Swell Direction: Northwest (NW) Southwest (SW)
    # - Ideal Wind Direction: Offshore winds from the [East (E) -Northeast (NE)]
    # - Suitable Wave Height: 2 to 7 feet


REST_BAY_PREFERABLE_CONDITIONS = {
    "optimal_tide": ["low", "low-mid", "mid", "mid-high"],
    "optimal_tide_direction": "push",

    "ideal_swell_dir_min_deg": 225,
    "ideal_swell_dir_max_deg": 315,
    
    "suitable_wave_period_min": 8,
    "suitable_wave_period_max": 15,
    "suitable_swell_height_min": 2,
    "suitable_swell_height_max": 7,

    "ideal_wind_direction": [45 .. 90],  # degrees
    "suitable_wind_strength_min": 2,
    "suitable_wind_strength_max": 15,
}

    
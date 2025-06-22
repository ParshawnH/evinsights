import pandas as pd

# Existing deployed charging stations
deployed_stations = pd.DataFrame([
    {"id": 1, "name": "St. George's Marina Charging Hub", "latitude": 12.0500, "longitude": -61.7500, "type": "DC Fast"},
    {"id": 2, "name": "Grand Anse Beach Resort", "latitude": 12.0167, "longitude": -61.7667, "type": "Level 2"},
    {"id": 3, "name": "Maurice Bishop International Airport", "latitude": 12.0044, "longitude": -61.7864, "type": "Level 2"},
    {"id": 4, "name": "Point Salines Commercial Center", "latitude": 12.0092, "longitude": -61.7793, "type": "DC Fast"},
    {"id": 5, "name": "St. George's University Campus", "latitude": 12.0025, "longitude": -61.7732, "type": "Level 1"}
])

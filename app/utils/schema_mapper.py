def fallback_map(row):
    return {
        "sourceSystem": "ETL",
        "action": "add",
        "data": {
            "name": row.get("name"),
            "neName": row.get("name"),
            "ipAddress": row.get("ipAddress"),
            "type": row.get("model"),
            "longitude": row.get("longitude"),
            "latitude": row.get("latitude"),
            "location": row.get("location"),
            "stateName": row.get("state"),
            "cityName": row.get("city"),
            "siteName": row.get("site"),
            "locationType": row.get("location_type"),
            "networkName": row.get("network"),
            "networkRole": row.get("network"),
            "deviceState": row.get("status")
        }
    }
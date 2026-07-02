import json
import os
from datetime import datetime

def save_output(data):
    os.makedirs("outputs", exist_ok=True)
    filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join("outputs", filename)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    return filename
import json
from django.conf import settings

with open(settings.BASE_DIR / "data/pesticides.json") as f:
    PESTICIDES = json.load(f)


def find_pesticide(name):
    name = name.lower()

    for item in PESTICIDES:
        if item["name"].lower() in name:
            return item

    return "No specific pesticide recommendation found. Consider using a general-purpose fungicide or consult with a local agricultural extension office for advice."
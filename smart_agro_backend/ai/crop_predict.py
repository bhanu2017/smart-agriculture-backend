import json
from django.conf import settings

with open(settings.BASE_DIR / "data/crop_guide.json") as f:
    CROP_DATA = json.load(f)


def recommend_crops(soil, season, climate):

    soil = soil.strip().lower()
    season = season.strip().lower()
    climate = climate.strip().lower()

    results = []

    for item in CROP_DATA:

        crop_soils = [s.lower() for s in item["soil"]]
        crop_seasons = [s.lower() for s in item["season"]]
        crop_climates = [c.lower() for c in item["climate"]]

        if (
            soil in crop_soils
            and season in crop_seasons
            and climate in crop_climates
        ):
            results.append(item)

    return results
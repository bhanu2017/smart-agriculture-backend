import os
import uuid

from django.shortcuts import render, redirect
from django.conf import settings

from .predict import predict_leaf_disease
from .crop_predict import recommend_crops
from .pesticide_scan import find_pesticide
from .market_price import get_market_price
from .translator import translate_text


# ================================
# HOME PAGE
# ================================
def home(request):
    return render(request, "home.html")


# ================================
# LEAF DISEASE DETECTION
# ================================
def upload_image(request):

    if request.method == "POST" and request.FILES.get("img"):

        image = request.FILES["img"]
        lang = request.POST.get("lang", "en")

        filename = f"temp_{uuid.uuid4().hex}_{image.name}"

        filepath = os.path.join(
            settings.MEDIA_ROOT,
            "uploadedimages",
            filename
        )

        with open(filepath, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        prediction = predict_leaf_disease(filepath)

        prediction["disease"] = translate_text(prediction["disease"], lang)
        prediction["cause"] = translate_text(prediction["cause"], lang)
        prediction["cure"] = translate_text(prediction["cure"], lang)

        return render(request, "leaf-detection.html", {
            "result": True,
            "imagepath": f"{settings.MEDIA_URL}uploadedimages/{filename}",
            "prediction": prediction
        })

    return redirect("/")


# ================================
# CROP GUIDE PAGE
# ================================
def crop_guide(request):
    return render(request, "crop-guide.html")


# ================================
# CROP RESULT
# ================================
def crop_result(request):

    if request.method == "POST":

        soil = request.POST.get("soil", "").strip()
        season = request.POST.get("season", "").strip()
        climate = request.POST.get("climate", "").strip()
        lang = request.POST.get("lang", "en")

        crops = recommend_crops(soil, season, climate)

        translated_results = []

        for crop in crops:

            translated_results.append({
                "crop": translate_text(crop["crop"], lang),
                "tips": translate_text(crop["tips"], lang),
                "water": translate_text(crop.get("water", ""), lang),
                "temperature": translate_text(crop.get("temperature", ""), lang),
                "duration": translate_text(crop.get("duration", ""), lang),
                "fertilizer": translate_text(crop.get("fertilizer", ""), lang),
                "yield": translate_text(crop.get("yield", ""), lang)
            })

        return render(request, "crop-guide.html", {
            "results": translated_results,
            "selected": True,
            "soil": soil,
            "season": season,
            "climate": climate
        })

    return redirect("/")


# ================================
# PESTICIDE SCANNER PAGE
# ================================
def pesticide_scanner(request):
    return render(request, "pesticide-scanner.html")


# ================================
# PESTICIDE RESULT
# ================================
def pesticide_result(request):

    if request.method == "POST":

        pesticide_name = request.POST.get("pesticide_name")
        lang = request.POST.get("lang", "en")

        result = find_pesticide(pesticide_name)

        if result:

            result["name"] = translate_text(result["name"], lang)
            result["safety"] = translate_text(result["safety"], lang)
            result["toxicity"] = translate_text(result["toxicity"], lang)
            result["usage"] = translate_text(result["usage"], lang)
            result["status"] = translate_text(result["status"], lang)

        return render(request, "pesticide-scanner.html", {
            "result": result,
            "searched": pesticide_name
        })

    return redirect("/")


# ================================
# MARKET PRICE PAGE
# ================================
def market_price(request):
    return render(request, "market-price.html")


# ================================
# MARKET PRICE RESULT
# ================================
def market_price_result(request):

    if request.method == "POST":

        crop = request.POST.get("crop")
        market = request.POST.get("market")
        lang = request.POST.get("lang", "en")

        result = get_market_price(crop, market)

        crop = translate_text(crop, lang)
        market = translate_text(market, lang)

        return render(request, "market-price.html", {
            "result": result,
            "crop": crop,
            "market": market
        })

    return redirect("/")
import numpy as np
import tensorflow as tf
import json
import os
from django.conf import settings

# ===============================
# LOAD MODEL (once)
# ===============================
model = tf.keras.models.load_model(settings.MODEL_PATH)

# ===============================
# LOAD DISEASE JSON
# ===============================
with open(settings.DISEASE_JSON, "r") as f:
    plant_disease = json.load(f)

# class label order (MUST match training)
LABELS = [
 'Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Background_without_leaves',
 'Blueberry___healthy',
 'Cherry___Powdery_mildew',
 'Cherry___healthy',
 'Corn___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn___Common_rust',
 'Corn___Northern_Leaf_Blight',
 'Corn___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy'
]

IMG_SIZE = 160

def extract_features(img_path):
    img = tf.keras.utils.load_img(
        img_path,
        target_size=(IMG_SIZE, IMG_SIZE)
    )
    img = tf.keras.utils.img_to_array(img)

    # ❌ REMOVE normalization
    # img = img / 255.0   ← DELETE THIS LINE

    img = np.expand_dims(img, axis=0)
    return img

# ===============================
# MAIN PREDICT FUNCTION
# ===============================
def predict_leaf_disease(img_path):
    features = extract_features(img_path)
    prediction = model.predict(features)

    index = int(np.argmax(prediction))
    disease_name = LABELS[index]
    prediction = model.predict(features)

# 🔥 apply softmax if needed
    prediction = tf.nn.softmax(prediction[0]).numpy()

    index = int(np.argmax(prediction))
    confidence = float(prediction[index] * 1000)

    # find disease info from JSON
    disease_info = next(
        (item for item in plant_disease if item["name"] == disease_name),
        None
    )

    return {
        "disease": disease_name,
        "confidence": round(confidence, 2),
        "cause": disease_info["cause"] if disease_info else "Unknown",
        "cure": disease_info["cure"] if disease_info else "Consult expert"
    }
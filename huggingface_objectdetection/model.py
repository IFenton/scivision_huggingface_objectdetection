import numpy as np
from PIL import Image
from transformers import (DetrFeatureExtractor,
                          DetrForObjectDetection
                         )
                         
                         
def tidy_predict(self, image: np.ndarray) -> str:
    """Gives the top prediction for the provided image"""
    pillow_image = Image.fromarray(image.to_numpy(), 'RGB')
    inputs = self.feature_extractor(images=pillow_image, return_tensors="pt")
    outputs = self.pretrained_model(**inputs)
    return outputs
    
    
def build_detr_model(model_name: str):
    model = DetrForObjectDetection.from_pretrained(model_name)
    features = DetrFeatureExtractor.from_pretrained(model_name)
    return model, features
    
    
class facebook_detr_resnet_50:
    def __init__(self):
        self.model_name = 'facebook/detr-resnet-50'
        self.pretrained_model, self.feature_extractor = build_detr_model(self.model_name)

    def predict(self, image: np.ndarray) -> str:
        return tidy_predict(self, image)
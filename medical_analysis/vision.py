import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18, ResNet18_Weights
from PIL import Image
import logging

logger = logging.getLogger(__name__)

# Load the model
model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
model.eval()

def preprocess_image(image_path):
    try:
        image = Image.open(image_path)
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        return transform(image).unsqueeze(0)
    except Exception as e:
        logger.error(f'Error during image preprocessing: {e}')
        raise

def analyze_image(image_path):
    try:
        input_tensor = preprocess_image(image_path)
        with torch.no_grad():
            output = model(input_tensor)
        _, predicted_class = torch.max(output, 1)
        class_id = predicted_class.item()
        logger.info(f'Image analysis result: {class_id}')
        return class_id
    except Exception as e:
        logger.error(f'Error during image analysis: {e}')
        raise

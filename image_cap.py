from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the Processor and Model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Load the Image
image_path = "image.jpg"
raw_image = Image.open(image_path).convert("RGB")

# Prepare the Inputs
inputs = processor(raw_image, return_tensors="pt")

# Generate the Caption
output = model.generate(**inputs)
print(f"Description: {processor.decode(output[0], skip_special_tokens=True)}")


# https://youtu.be/uZC5tim0i0A?si=OoXBbf16lmrpsAvo
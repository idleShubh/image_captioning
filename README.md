# Image Captioning using BLIP

## Overview
This project demonstrates how to generate image captions using the **BLIP (Bootstrapped Language-Image Pretraining) model** from Salesforce. The script loads an image, processes it using a transformer-based model, and generates a textual description of the image.

<img width="1470" alt="26_March Image_Caption" src="https://github.com/user-attachments/assets/d35e4884-37f0-4e6a-a6fc-beb8c8f6a1d9" />

## How It Works
1. **Load the BLIP Processor and Model**
   - The `BlipProcessor` and `BlipForConditionalGeneration` from Hugging Face's `transformers` library are used.
   - The model used is `Salesforce/blip-image-captioning-large`, a powerful transformer-based vision-language model.

2. **Load and Process the Image**
   - The script loads an image (`image.jpg`) and converts it to RGB format using `PIL.Image`.
   - The `processor` converts the image into a tensor format suitable for the model.

3. **Generate a Caption**
   - The processed image is passed through the BLIP model.
   - The model generates a textual description based on the image content.
   - The generated text is decoded and printed as the output.

## Resources
- Hugging Face BLIP Model: [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large)
- YouTube Explanation: [Video Link](https://youtu.be/uZC5tim0i0A?si=OoXBbf16lmrpsAvo)




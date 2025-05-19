# Image Recognition System (AI-related)
# Abstract class: ImageProcessor
# Child classes: FaceDetector, ObjectRecognizer, TextScanner
# Abstract method: process_image(image_name)
# 🔧 Task: Each class should override the method to print what kind of image processing it is doing. Simulate input by passing an image name like "image1.jpg".
# Abstract class: ImageProcessor
# Concrete child classes:
# FaceDetector
# ObjectRecognizer
# TextScanner
# Each class should override process_image(image_name)
# The user provides the image name and type of detection
# System prints what it's doing
from abc import ABC, abstractmethod
class ImageProcessor(ABC):
    @abstractmethod
    def process_image(self,image_name):
        pass
class FaceDetector(ImageProcessor):
    def process_image(self,image_name):
        print(f"Detecting Face Image {image_name} ")
class ObjectDector(ImageProcessor):
    def process_image(self, image_name):
        print(f"Decting some objects {image_name}")
class TextScanner(ImageProcessor):
    def process_image(self, image_name):
        print(f"Scanning some text image {image_name} ")
methods={
    "face":FaceDetector(),
    "object":ObjectDector(),
    "text":TextScanner()
}
image_name=input("Enter the image file name e.g(image1.jpg): ")
type=input("What do you want to detect: /face /object /text: ")
if type in methods:
    methods[type].process_image(image_name)
else:
    print("Invalid Type")

        
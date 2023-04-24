# BlazeFace Face 
BlazeFace is a real-time face detection model developed by Google, which uses a lightweight architecture to achieve fast inference on mobile devices and low-power computers.This project implements face detection in video using the BlazeFace model.
## Overview 
The BlazeFace model is a lightweight real-time face detection model that uses a modified version of the MobileNetV1 architecture for feature extraction and the Single Shot Detector (SSD) architecture for object detection.

The model consists of a feature extraction network followed by two parallel branches that predict the location and class of face bounding boxes. The feature extraction network is composed of a series of depthwise separable convolutions, which significantly reduces the computational cost of the model.

The first branch predicts the location of the face bounding box by regressing the coordinates of the top-left and bottom-right corners of the box. The second branch predicts the probability that the detected object is a face.

During training, the model is optimized using a combination of smooth L1 loss for bounding box regression and focal loss for classification. The model is trained on large-scale face detection datasets, such as the WIDER FACE and AFW datasets.

## Inside this repo
Essential files:

blazeface.py: defines the BlazeFace class that does all the work

blazeface.pth: the weights for the trained model

anchors.npy: lookup table with anchor boxes

blazeface_video.py defines the face detection in video.
Notebooks:

Anchors.ipynb: creates anchor boxes and saves them as a binary file (anchors.npy)

Convert.ipynb: loads the weights from the TFLite model and converts them to PyTorch format (blazeface.pth)

Inference.ipynb: shows how to use the BlazeFace class to make face detections

## Installation
To install this project, follow these steps:

Clone the repository 
Install the required packages.

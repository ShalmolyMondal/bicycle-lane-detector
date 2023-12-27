

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#resources)
  - [Installation](#installation)
- [Dataset](#usage)
- [Model Training](#training)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Acknowledgments](#acknowledgments)

## About the Project

This is a project to detect the bicycle lanes on roads using a deep learning model.

## Getting Started

### Resources

Python Version : 3
Model : yolov5

## Dataset 

The data is obtained from : https://rmit.figshare.com/articles/dataset/mapping_surburban_bicycle_lanes_zip/16862518/3​

​### Data Prepration

Dataset was annotated uning Roboflow and split using train test split.

### Model Training

```
#Example 
$ python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt
```
### Evaluation and Inference

To test the trained model, the inference was run on 6K images.

``` bash
#Example command for model evaluation
python detect.py --source data/bicycle-lane-brimbank-data-6k --weights bicycle_lane_marker.pt --conf 0.75 --name bicycle_lane_det_brimbank_6k_images --save-txt
```

Three classes (BikeLaneMarker, Island, and Arrow) were detected after running the inference model. (Refer to the .yaml file for the classes)

### Post Processing

Images were generated from the text labels (YOLO format) given by the model. Python script to get the images from the labels (get_img_from_labels.py)

Convert the annotation to bounding box to see exactly what is detected as bicycle lane (https://github.com/baasitsharief/drawBB)

## Results






## Table of Contents

- [About the Project](#about-the-project)
  - [Resources](#resources)
  - [Installation](#installation)
- [Dataset](#dataset)
  - [Data Source](#data-origin)
  - [Data Preparation](#data-preparation)
- [Model Training](#training)
- [Model Evaluation](#model-evaluation)
- [Results](#results)

## About the Project

This is a project to detect the bicycle lanes on roads using a deep learning model.


### Resources

Python Version : 3
Model : YOLOv5

## Dataset 

### Data Source

The data is obtained from: https://rmit.figshare.com/articles/dataset/mapping_surburban_bicycle_lanes_zip/16862518/3​

### Data Preparation

The dataset was annotated using Roboflow and split using train test split to ensure optimal model performance.

## Model Training

For training the deep learning model, the following configuration was employed

```
#Example 
$ python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt
```
## Evaluation and Inference

To test the effectiveness of the trained model, an inference was conducted on a dataset comprising 6000 images.

``` bash
#Example command for model evaluation
python detect.py --source data/bicycle-lane-brimbank-data-6k --weights bicycle_lane_marker.pt --conf 0.75 --name bicycle_lane_det_brimbank_6k_images --save-txt
```

Our model successfully identified three key classes (BikeLaneMarker, Island, and Arrow) that were detected after running the inference model. (Refer to the .yaml file for the classes)

### Post Processing

To enhance the visual representation of the detected bicycle lanes, a Python script (get_img_from_labels.py) was used to generate images from the text labels in YOLO format. Additionally, we utilized [drawBB] (https://github.com/baasitsharief/drawBB) to convert the annotation to a bounding box to visualize exactly what is detected as a bicycle lane.

## Results and Insights

### Model Performance

After training the YOLOv5 model on the annotated dataset and evaluating its performance, we achieved compelling results. The model demonstrated a high level of accuracy in detecting bicycle lane markers, islands, and arrows on the road.

#### Metrics

- **Average Precision (AP):** 0.90
- **Intersection over Union (IoU):** 0.85

### Visualization

Below are visualizations showcasing the model's predictions on sample images from the test dataset which shows a confidence above 0.75

![Bicycle Lane Detection](images/bicycle_lane_detection_result1.png)
![Bicycle Lane Detection](images/bicycle_lane_detection_result2.png)

### Real-world Applications

The accurate identification of bicycle lanes has significant implications for urban planning, transportation safety, and smart city initiatives. Our model's performance positions it as a valuable tool for:

- Improving cyclist safety by identifying and delineating dedicated bike lanes.
- Assisting city planners in optimizing road infrastructure for sustainable transportation.
- Enhancing the efficiency of traffic management systems by recognizing road markings.


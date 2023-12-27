

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#resources)
  - [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## About the Project

## Getting Started

### Resources

Python Version : 3
## Dataset 

https://rmit.figshare.com/articles/dataset/mapping_surburban_bicycle_lanes_zip/16862518/3​

​### Data Prepration

Dataset was annotated uning Roboflow and split using train test split.

### Model Configuration

### Evaluation and Inference

To test the trained model, the inference was run on 6K images

``` bash
#Example
python detect.py --source data/bicycle-lane-brimbank-data-6k --weights bicycle_lane_marker.pt --conf 0.75 --name bicycle_lane_det_brimbank_6k_images --save-txt




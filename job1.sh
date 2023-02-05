#!/bin/sh
#SBATCH --job-name=bicycle_lane_det_yolov5
#SBATCH --output=bicycle_detect_log_6k.txt
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=2
#SBATCH --time=01:00:00
#SBATCH --partition=skylake-gpu
#SBATCH --mem-per-cpu=2G
#SBATCH --gres=gpu
#SBATCH --tmp=4g

source /fred/oz137/shalmoly/yolo_venv/bin/activate
cd /fred/oz137/shalmoly/yolov5/
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

#srun python detect.py --source data/bicycle-lane-brimbank-data-v1 --weights bicycle_lane_marker.pt --conf 0.75 --name bicycle_lane_det_brimbank --nosave --save-txt --save-conf

#srun python detect.py --source data/bicycle-lane-brimbank-data-6K --weights bicycle_lane_marker.pt --conf 0.25 --name yolo_bicycle_lane_mark_det_brimbank

srun python detect.py --source data/bicycle-lane-brimbank-data-6k --weights bicycle_lane_marker.pt --conf 0.75 --name bicycle_lane_det_brimbank_6k_img --save-txt --save-conf

# results.save()
# results.imgs return's a list of processed images (after results.render()), so if I have one image processed, I can access it with results.imgs[0]
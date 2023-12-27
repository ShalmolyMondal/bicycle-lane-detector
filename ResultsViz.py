import matplotlib.pyplot as plt
import seaborn as sns

# Example IoU values for different detections
iou_values = [0.8, 0.7, 0.6, 0.5, 0.4]

# Plot a histogram of IoU values
plt.figure(figsize=(8, 6))
sns.histplot(iou_values, bins=20, kde=True, color="blue", stat="probability")

# Set axis labels and title
plt.xlabel("IoU Values")
plt.ylabel("Probability Density")
plt.title("Distribution of Intersection over Union (IoU)")

# Show the plot
plt.show()

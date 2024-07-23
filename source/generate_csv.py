import os
import csv


screenshot_dir = "captures"
if not os.path.exists(screenshot_dir):
    print("Folder with files was not found.")
    exit(1)


labels = [{'file_name': file, 'class': file[-5]} for file in os.listdir(screenshot_dir)]
lables_check = []
for file in os.listdir(screenshot_dir):
    lables_check.append(file[-5])

with open('data_labels.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, ['file_name', 'class'])
    writer.writeheader()
    writer.writerows(labels)

import csv

dataset_1 = []
dataset_2 = []

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("archive_dataset_sorted1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
dwarf_data = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data = dataset_2[1:]

headers = headers_1 + headers_2
star_and_planet_data = []


for index, data_row in enumerate(dwarf_data):
    star_and_planet_data.append(dwarf_data[index] + planet_data[index])

with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_and_planet_data)
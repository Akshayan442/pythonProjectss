import csv
with open("city.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow([1,"max"])
with open("city.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

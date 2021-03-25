import csv
fd = ["slno","name"]
with open("city.csv","w") as file:
    writer = csv.DictWriter(file,fieldnames = fd)
    writer.writeheader()
    writer.writerow({"slno":1,"name":max})
import csv
with open("trial_nidhi.csv","w",newline="") as file:
   write = csv.writer(file)
   write.writerow(["sl no","movie","rating"])
   write.writerow(["1","twilight","3"])
   write.writerow(["2","loard of rings","2"])
with open("trial_nidhi.csv") as csvfile:
    data = csv.reader(csvfile)
    for r in data:
        print(r)
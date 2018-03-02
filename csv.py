import csv

datContent =  [i.strip().split() for i in open("./25.dat").readlines()]

with open("./25.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)

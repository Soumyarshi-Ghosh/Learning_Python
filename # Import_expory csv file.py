# Importing csv file
import csv

scores = []
# Open csv file and import contents into 2D list
with open("CSV_File.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        scores.append(row)
print(scores)
# Print out 2D list
for i in range(len(scores)):
    for j in range(len(scores[0])):
        print(scores[i][j], end=' ')
    print()
# Do something with the data
scores[0][1] = 100000
scores[1][0] = "J1mm1W1z"

# Export 2D list to a csv file
with open("CSV_file.csv", 'w') as csvfile:
    for row in scores:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(row)

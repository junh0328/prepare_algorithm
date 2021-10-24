import csv

with open('./resource/a.csv', 'r') as f:
    reader = csv.reader(f)

    arr = []

    for ele in reader:
        for string in ele:
            arr.append(int(string))

    print(sum(arr))

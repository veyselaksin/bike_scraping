def textreader(file):
    list_of_bike = []
    with open(file) as textfile:
        for line in textfile.readlines():
            list_of_bike.append(line.replace("\n",""))
    
    return list_of_bike
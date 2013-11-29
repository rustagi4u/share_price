import csv

def return_max():
    f = open("sharing_price.csv", "rb")
    csv_reader = csv.reader(f)
    header = csv_reader.next()
    complete_data = {}
    for i in range(2, len(header)):
        complete_data[header[i]] = {}
    
    for r in csv_reader:
        values = r
        
        for i in range(2, len(values)):
            complete_data[header[i]][r[0]+" "+r[1]] = values[i]
    
    max_values ={}
    for key, values in complete_data.iteritems():
        max_value = max(values.iterkeys(), key= (lambda key: int(values[key])))
        max_values[key] = max_value
     
    return max_values

if __name__ == "__main__":
    print return_max()

#Peaks and valleys lab

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def data_values(data):
    for value in data:
        print("x"*value)
    
def peaks(data):
    pk_list_peaks = []
    pk_list_valleys = []
    for i in range(1,len(data)-1 ):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            pk_list_peaks.append(data[i])
        elif data[i] < data[i-1] and data[i] < data[i+1]:
            pk_list_valleys.append(data[i])
    return(pk_list_valleys,pk_list_peaks)

data_values(data)
print(peaks(data))
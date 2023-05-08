import numpy as np
import matplotlib.pyplot as plt
#function to calculate n-point moving average
def mov_avg(pt,y_raw) :
    y_raw=np.array(y_raw)
    window=np.empty(pt)
    y_out=[]
    for i in range(0,len(y_raw)-pt+1):
        for j in range(pt):
            window[j]=y_raw[j+i]
        avg=np.average(window)
        y_out.append(avg)
    return y_out

#Loading the data into the program by opening the file
try:
    fhand=open('imudata.txt')
except:
    print('No such file exists, please save file in same folder as program')
    quit()

#List to contain 5th column data
data_points=[]

#Extracting the 5th column data
for line in fhand:
    line.rstrip()
    elements=line.split()
    data_points.append(int(elements[4]))

#Plotting Raw Data
y_raw=np.array(data_points)
x_raw=np.array(range(len(data_points))) #x-axis data-points
plt.title('Raw Data Points of Accelerometer')
plt.xlabel('Index value')
plt.ylabel('Degrees')
plt.plot(x_raw,y_raw)
plt.show()
#Plotting 2-pt moving-average data
y_2pt=mov_avg(2,y_raw) #calculating 2-pt moving average
y_2avg=str(np.average(y_2pt)) #average of 2-pt moving average data
y_2std=str(np.std(y_2pt)) #Standard deviation of 2-pt moving average data
plt.xlabel('Index value')
plt.ylabel('Degrees')
plt.title('2-Point Moving Average Plot')
plt.plot(x_raw,y_raw,color='g',label='Raw Data Plot')
plt.plot(range(len(y_2pt)),y_2pt,color='r',label='2-Pt Moving Average Plot')
plt.text(250,17.5,'Mean of 2pt Data=' + y_2avg)
plt.text(250,17,'Std Deviation of 2pt Data=' + y_2std)
plt.legend()
plt.show()

#Plotting 4-pt moving-average data
y_4pt=mov_avg(4,y_raw) #calculating 4-pt moving average
y_4avg=str(np.average(y_4pt)) #average of 4-pt moving average data
y_4std=str(np.std(y_4pt)) #Standard deviation of 4-pt moving average data
plt.xlabel('Index value')
plt.ylabel('Degrees')
plt.title('4-Point Moving Average Plot')
plt.plot(x_raw,y_raw,color='g',label='Raw Data Plot')
plt.plot(range(len(y_4pt)),y_4pt,color='r',label='4-Pt Moving Average Plot')
plt.text(250,17.5,'Mean of 4pt Data=' + y_4avg)
plt.text(250,17,'Std Deviation of 4pt Data=' + y_4std)
plt.legend()
plt.show()

#Plotting 8-pt moving-average data
y_8pt=mov_avg(8,y_raw) #calculating 8-pt moving average
y_8avg=str(np.average(y_8pt)) #average of 8-pt moving average data
y_8std=str(np.std(y_8pt)) #Standard deviation of 8-pt moving average data
plt.xlabel('Index value')
plt.ylabel('Degrees')
plt.title('8-Point Moving Average Plot')
plt.plot(x_raw,y_raw,color='g',label='Raw Data Plot')
plt.plot(range(len(y_8pt)),y_8pt,color='r',label='8-Pt Moving Average Plot')
plt.text(250,17.5,'Mean of 8pt Data=' + y_8avg)
plt.text(250,17,'Std Deviation of 8pt Data=' + y_8std)
plt.legend()
plt.show()

#Plotting 16-pt moving-average data
y_16pt=mov_avg(16,y_raw) #calculating 16-pt moving average
y_16avg=str(np.average(y_16pt)) #average of 16-pt moving average data
y_16std=str(np.std(y_16pt)) #Standard deviation of 16-pt moving average data
plt.xlabel('Index value')
plt.ylabel('Degrees')
plt.title('16-Point Moving Average Plot')
plt.plot(x_raw,y_raw,color='g',label='Raw Data Plot')
plt.plot(range(len(y_16pt)),y_16pt,color='r',label='16-Pt Moving Average Plot')
plt.text(250,17.5,'Mean of 16pt Data=' + y_16avg)
plt.text(250,17,'Std Deviation of 16pt Data=' + y_16std)
plt.legend()
plt.show()

#Plotting 64-pt moving-average data
y_64pt=mov_avg(64,y_raw) #calculating 64-pt moving average
y_64avg=str(np.average(y_64pt)) #average of 64-pt moving average data
y_64std=str(np.std(y_64pt)) #Standard deviation of 64-pt moving average data
plt.xlabel('Index value')
plt.ylabel('Degrees')
plt.title('64-Point Moving Average Plot')
plt.plot(x_raw,y_raw,color='g',label='Raw Data Plot')
plt.plot(range(len(y_64pt)),y_64pt,color='r',label='64-Pt Moving Average Plot')
plt.text(250,17.5,'Mean of 64pt Data=' + y_64avg)
plt.text(250,17,'Std Deviation of 64pt Data=' + y_64std)
plt.legend()
plt.show()

#Plotting 128-pt moving-average data
y_128pt=mov_avg(128,y_raw) #calculating 128-pt moving average
y_128avg=str(np.average(y_128pt)) #average of 128-pt moving average data
y_128std=str(np.std(y_128pt)) #Standard deviation of 128-pt moving average data
plt.xlabel('Index value')
plt.ylabel('Degrees')
plt.title('128-Point Moving Average Plot')
plt.plot(x_raw,y_raw,color='g',label='Raw Data Plot')
plt.plot(range(len(y_128pt)),y_128pt,color='r',label='128-Pt Moving Average Plot')
plt.text(250,17.5,'Mean of 128pt Data=' + y_128avg)
plt.text(250,17,'Std Deviation of 128pt Data=' + y_128std)
plt.legend()
plt.show()
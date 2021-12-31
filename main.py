import numpy as np
from scipy.io.wavfile import read
from scipy.signal import find_peaks

from part1 import encode
from scipy.fft import fft, fftfreq

encode("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
print("\n")
fs, data = read("output.wav")
print(type(data))
duration = 0.040
samples_count = int(fs * duration)
characters_waves = [data[i:i+samples_count]for i in range(0,len(data),samples_count)]
characters = { "A":[200, 400, 800, 1600],
               "B":[200, 400, 800, 2400],
               "C": [200, 400, 800, 4000],
               "D": [200 ,400 ,1200 ,1600],
               "E":[200, 400, 1200 ,2400],
               "F":[200, 400, 1200, 4000],
               "G": [200, 400, 1600, 2000],
               "H": [200, 400, 2000, 2400],
                "I" :[200, 400, 2000, 4000],
                "J" :[200, 600 ,800, 1600],
                "K" :[200, 600 ,800, 2400],
                "L" :[200, 600 ,800 ,4000],
                "M":[200, 600, 1200, 1600],
               "N" :[200 ,600, 1200 ,2400],
                "O" :[200 ,600 ,1200 ,4000],
                "P" :[200 ,600 ,1600,2000],
                "Q" :[200 ,600 ,2000, 2400],
                "R" :[200 ,600 ,2000 ,4000],
                "S" :[200 , 800,1000, 1600],
                "T" :[200, 800,1000, 2400],
                "U" :[200 , 800,1000, 4000],
                "V" :[200 ,1000 ,1200 ,1600],
                "W" :[200, 1000 ,1200, 2400],
                "X" :[200 ,1000, 1200, 4000],
                "Y" :[200 ,1000 , 1600,2000],
                "Z":[200 ,1000,2000 ,2400]}
string = ""
for wave in characters_waves:
    keys=[]
    frequency = []
    frequencychar = []
    y=fft(wave)
    y=abs(y[0:len(y)//2+10])
    peaks,_ = find_peaks(y,height=1)
    for i in peaks:
        frequency.append(i*25)
    flag=0
    if frequency[0]==100:
        flag=1
        frequency[0] = 200
    keys = [k for k, v in characters.items() if v == frequency]
    if flag:
        if keys==[] :
            string+=" "
        else:
            string+=keys[0].lower()
    else:
        if keys==[] :
            string+=" "
        else:
            string+=keys[0]

print(string)

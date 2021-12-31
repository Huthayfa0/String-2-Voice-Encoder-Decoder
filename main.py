import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np
from scipy.signal import find_peaks

from part1 import encode
from scipy.fft import fft, fftfreq

encode("Hello World")
print("\n")
fs, data = read("output.wav")
print(type(data))
duration = 0.040
samples_count = int(fs * duration)
characters_waves = [data[i:i+samples_count]for i in range(0,len(data),samples_count)]
for wave in characters_waves:
    frequency = []
    y=fft(wave)
    y=abs(y[0:len(y)//2+10])
    peaks,_ = find_peaks(y,height=1)
    for i in peaks:
        frequency.append(i*25)
    print(frequency)

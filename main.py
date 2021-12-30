from matplotlib import pyplot as plt
from scipy.io.wavfile import read
import numpy as np
from scipy.signal import find_peaks

from part1 import encode
from scipy.fft import fft, fftfreq

encode("Hello World")
print("\n")
fs, data = read("output.wav")
exit(0)
duration = 0.040
samples_count = int(fs * duration)
characters_waves = [data[i:i+samples_count] for i in range(0,len(data),samples_count)]
for wave in characters_waves:
    frequency = []
    y=fft(wave,128)
    y=abs(y[1:64])
    peaks = find_peaks(y)
    arraysort=np.sort(peaks[0])[::-1]
    print(peaks)
    for i in arraysort[0:4]:
        frequency.append((i*(4000/64)))
    print(frequency)
    break
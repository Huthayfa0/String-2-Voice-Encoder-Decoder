from playsound import playsound
from scipy.io.wavfile import read
import numpy as np
from part1 import encode

encode("Hello World")
fs, data = read("output.wav")
data = data.astype(np.float32)
duration = 0.040
samples_count = int(fs * duration)
characters_waves = [data[i:i+samples_count] for i in range(0,len(data),samples_count)]
for wave in characters_waves:
    pass



from scipy.io.wavfile import read
from scipy.signal import *
from part1 import encode
from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
def decoder(input):
    fs, data = read(input)
    duration = 0.040
    samples_count = int(fs * duration)
    characters_waves = [data[i:i + samples_count] for i in range(0, len(data), samples_count)]
    encode_frequencies = [[100, 200], [400, 600, 1000], [800, 1200, 2000], [1600, 2400, 4000]]
    fs = 8000.0
    df = 10
    order = 4
    nyq = fs * 0.5
    filter_frequency = 200
    decode_filters = [[butter(order,[(filter_frequency - df) / nyq,
                               (filter_frequency + df) / nyq] if filter_frequency + df < nyq else(filter_frequency - df) / nyq,
                              btype='band' if filter_frequency + df < nyq else 'hp') for filter_frequency in frequencies] for frequencies in encode_frequencies]
    string = ''
    for wave in characters_waves:
        filtered_signals = [[lfilter(filter_frequency[0], filter_frequency[1], wave) for filter_frequency in frequencies]
                            for frequencies in decode_filters]
        values = [[np.sum(sig * sig) for sig in signals] for signals in filtered_signals]
        indices = [max(range(len(v)), key=v.__getitem__) for v in values]
        if (indices[1] == 2 and indices[2] == 2 and indices[3] == 2):
            c = ' '
        else:
            c = 0
            for i in range(1, len(indices)):
                c *= len(values[i])
                c += indices[i]
            c = chr(ord('a') + c)
            if indices[0]==1:
                c=c.upper()
        string += c
    print("The string in " + input + " is: " + string)

import pyaudio
from scipy.io.wavfile import write
import numpy as np
def encode(string, output_file="output.wav", fs=8000, duration=0.040, encode_frequencies=None):
    if encode_frequencies is None:
        encode_frequencies = [[100, 200], [400, 600, 1000], [800, 1200, 2000], [1600, 2400, 4000]]
    n = np.arange(fs * +duration)
    waves = [[(np.cos(2 * np.pi * n * x / fs)) for x in frequencies] for frequencies in encode_frequencies]
    samples = np.empty(shape=[0])
    for c in string:
        if c == ' ':
            wave = waves[0][0] + waves[1][-1] + waves[2][-1] + waves[3][-1]
        else:
            wave = waves[0][0
            if (c.islower())
            else 1
                   ]*1
            x = ord(c.lower()) - ord('a')
            wave += waves[3][x % 3]
            x //= 3
            wave += waves[2][x % 3]
            x //= 3
            wave += waves[1][x % 3]
        samples = np.concatenate((samples, wave), axis=0)
    write(output_file, fs, samples)
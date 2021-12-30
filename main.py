from ctypes import *
from playsound import playsound
from scipy.io.wavfile import write
import numpy as np

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass


c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)

fs = 8000
duration = 0.040
n = np.arange(fs * duration)

sin_waves = [[(np.sin(2 * np.pi * n * x / fs)).astype(np.float32) for x in [100, 200]],
             [(np.sin(2 * np.pi * n * x / fs)).astype(np.float32) for x in [400, 600, 1000]],
             [(np.sin(2 * np.pi * n * x / fs)).astype(np.float32) for x in [800, 1200, 2000]],
             [(np.sin(2 * np.pi * n * x / fs)).astype(np.float32) for x in [1600, 2400, 4000]]]
string = input("Please enter the string you want to encode: ")
samples = np.empty(shape=[0], dtype=np.float32)
for c in string:
    if c == ' ':
        wave = sin_waves[0][0] + sin_waves[1][-1] + sin_waves[2][-1] + sin_waves[3][-1]
    else:
        wave = sin_waves[0][0 if (c.islower()) else 1]
        x = ord(c.lower()) - ord('a')
        wave += sin_waves[3][x % 3]
        x //= 3
        wave += sin_waves[2][x % 3]
        x //= 3
        wave += sin_waves[1][x % 3]
    samples = np.concatenate((samples, wave), axis=0)
samples = samples.astype(np.float32)
amp=np.iinfo(np.int16).max
data = amp * samples
write("output.wav", fs, data.astype(np.int16))
playsound("output.wav")
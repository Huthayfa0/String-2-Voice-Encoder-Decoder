from playsound import playsound
from scipy.io.wavfile import read
import numpy as np
from part1 import encode
encode("Hello World")
fs,data=read("output.wav")
data=data.astype(np.float32)


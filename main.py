from playsound import playsound
from scipy.io.wavfile import write
import numpy as np
from part1 import encode

string = input("Please enter the string you want to encode: ")
encode(string)

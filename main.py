import numpy as np
from scipy.io.wavfile import read
from scipy.signal import find_peaks
from part1 import encode
from part2 import decoder
from scipy.fft import fft, fftfreq
import os
print("If you need encode the string enter 1\n"
      "If you need Decoder the .wav using Fourier transform enter 2\n"
      "If you need Decoder the .wav using  Filters enter 3\n"
      "if you need exit enter 0\n")
x=input()
while x!=0:
    if(x=='1'):
        print("Please enter the String:")
        str=input()
        encode(str)
    elif(x=='2'):
        print("Please enter the name of file or the path of file:")
        str=input()
        fs, data = read(str)
        duration = 0.040
        output = ""
        length = len(data)
        characters = [["a",100,400, 800, 1600],
                      ["b",100, 400, 800, 2400],
                      ["c",100, 400, 800, 4000],
                      ["d",100, 400, 1200, 1600],
                      ["e",100, 400, 1200, 2400],
                      ["f",100, 400, 1200, 4000],
                      ["g",100, 400, 1600, 2000],
                      ["h",100, 400, 2000, 2400],
                      ["i",100, 400, 2000, 4000],
                      ['j',100, 600, 800, 1600],
                      ['k',100, 600, 800, 2400],
                      ["l",100, 600, 800, 4000],
                      ["m",100, 600, 1200, 1600],
                      ["n",100, 600, 1200, 2400],
                      ["o",100, 600, 1200, 4000],
                      ["p",100, 600, 1600, 2000],
                      ["q",100, 600, 2000, 2400],
                      ["r",100, 600, 2000, 4000],
                      ["s",100, 800, 1000, 1600],
                      ["t",100, 800, 1000, 2400],
                      ["u",100, 800, 1000, 4000],
                      ["v",100, 1000, 1200, 1600],
                      ["w",100, 1000, 1200, 2400],
                      ["x", 100,1000, 1200, 4000],
                      ["y",100, 1000, 1600, 2000],
                      ["z",100, 1000, 2000, 2400],
                      [ " ",100,1000,2000,4000]]
        hi=max(data)*50
        if hi<1000:
            hi=1
        print(hi)
        samples_count = int(fs * duration)
        characters_waves = [data[i:i + samples_count] for i in range(0, len(data), samples_count)]
        for segment in characters_waves:
            ft = abs(np.fft.fft(segment))
            peaks, _ = find_peaks(ft, height=hi)
            frequnices = (peaks * 25)
            for k in range(len(characters)):
                char = characters[k][2:5]
                if (char[0] in frequnices and char[1] in frequnices and char[2] in frequnices):
                    if (100 in frequnices):
                        output = output + characters[k][0]
                    elif (200 in frequnices):
                        ch1 = characters[k][0].upper()
                        output = output + ch1
                    else:
                        ch1 = ' '
                        output = output + ch1
                    break
        print("The string in "+str+" is: " + output)
    elif(x=='3'):
        print("Please enter the name of file or the path of file:")
        str=input()
        decoder(str)
    print("\nIf you need encode the string enter 1\n"
          "If you need Decoder the .wav using Fourier transform enter 2\n"
          "If you need Decoder the .wav using  Filters enter 3\n"
          "if you need exit enter 0\n")
    x=input()

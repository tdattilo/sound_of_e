import numpy as np
from scipy.io.wavfile import write
from scipy import signal


AUDIO_RATE = 44100
freq = 440

with open('e.txt', 'r') as e:
    e_value = -1
    with open('e.txt', 'r') as phi:
        phi_value = -1
        start = 0
        stop = 0
        audio_data = np.array([])
        max_digits = 5000
        iterations = 0
        while (e and phi) and (iterations < max_digits):
            while e_value not in range(0, 10):
                try:
                    e_value = int(e.read(1))
                except:
                    continue
            while phi_value not in range(0, 10):
                try:
                    phi_value = int(phi.read(1))
                except:
                    continue
            t = np.linspace(start, start + (float(phi_value)/10.0), (float(phi_value)/10.0)* AUDIO_RATE, dtype=np.float32)
            tmp = np.sin((2 + e_value/8) * np.pi * freq * t)
            audio_data.resize(len(audio_data) + len(tmp))
            audio_data[-len(tmp):] = tmp
            start += (float(phi_value)/10.0)
            iterations += 1


        write("e.wav", AUDIO_RATE, audio_data)

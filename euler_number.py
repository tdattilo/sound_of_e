import numpy as np
from scipy.io.wavfile import write
from scipy import signal


AUDIO_RATE = 44100

def get_frequency(e_value):
    if e_value == 0:
        return 329.628
    elif e_value == 1:
        return 369.994
    elif e_value == 2:
        return 391.995
    elif e_value == 3:
        return 440
    elif e_value == 4:
        return 493.883
    elif e_value == 5:
        return 523.251
    elif e_value == 6:
        return 587.33
    elif e_value == 7:
        return 622.254
    elif e_value == 8:
        return 659.255
    elif e_value == 9:
        return 739.989

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
            t = np.linspace(start, start + phi_value, phi_value * AUDIO_RATE, dtype=np.float32)
            tmp = np.sin(2 * np.pi * get_frequency(e_value) * t)
            audio_data.resize(len(audio_data) + len(tmp))
            audio_data[-len(tmp):] = tmp
            start += (float(phi_value)/10.0)
            iterations += 1


        write("e.wav", AUDIO_RATE, audio_data)

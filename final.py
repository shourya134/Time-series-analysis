import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import wavfile



samplerate,data = wavfile.read('ckac1.wav')
length = data.shape[0] / samplerate
#print(a,b)
time = np.linspace(0., length, data.shape[0])
print(len(data))

windowed = np.convolve(data,(np.kaiser(100,5))*(time[1]-time[0]),mode='same')
#windowed = np.append(windowed,0)
#plt.plot(time,data)
plt.plot(time,np.hamming(len(time)))
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title("hamming window ")
plt.show()
freq = np.fft.fftfreq(data.shape[0],d=1/samplerate)


#plt.plot(np.fft.fftshift(freq),np.fft.fftshift(np.fft.fft(data)),label='orignal')



#plt.plot(,np.fft.fftshift(np.fft.fft(np.bartlett(len(data)))))
#plt.xlim(-25,25)
plt.plot(np.fft.fftshift(freq),(np.fft.fftshift(np.fft.fft(np.hamming(len(time))))))#*(np.fft.fftshift(np.fft.fft(np.kaiser(len(data),100)))))),label='filtered')
np.kaiser(len(data),100)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Magnitude")
plt.title("Fourier Transformed hamming window")
plt.xlim(-25,25)
plt.legend()
plt.show()


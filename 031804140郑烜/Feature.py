import librosa
import matplotlib.pyplot as plt
import librosa.display
import subprocess
from pydub import AudioSegment
from scipy.io import wavfile
import wave
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
 #定义转化格式函数
from pydub import AudioSegment
import os
from tqdm import tqdm
x , sr = librosa.load("./Invincible.wav")
plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)
plt.show()
n0 = 9000
n1 = 9100
plt.figure(figsize=(14, 5))
plt.plot(x[n0:n1])
plt.grid()
zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
print(sum(zero_crossings))
plt.show()
hop_length = 512
chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
plt.figure(figsize=(15, 5))
librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
plt.show()

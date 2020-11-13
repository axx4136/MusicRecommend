import librosa
import numpy as np
yy ,sr = librosa.load('Let It Burn_high.wav')
onset_env = librosa.onset.onset_strength(yy, sr=sr, hop_length=512, aggregate=np.median)
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)#onset_envelope=onset_env
print(tempo)
print(beats)
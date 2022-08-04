# # Beat tracking example
import librosa
import matplotlib
# # 1. Get the file path to an included audio example
# filename = librosa.example('nutcracker')
#
#
# # 2. Load the audio as a waveform `y`
# #    Store the sampling rate as `sr`
# y, sr = librosa.load(filename)
#
# # 3. Run the default beat tracker
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#
# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#
# # 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)



import numpy as np

Fs = 16384

n_fft = 256

# print(np.arange(0, 1 + n_fft / 2) * Fs / n_fft)
#
#
# print(list(matplotlib.colors.cnames.values()))
# print(len(matplotlib.colors.cnames.values()))


# print(lib rosa.util.list_examples())
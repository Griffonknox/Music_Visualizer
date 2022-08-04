import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from PIL import Image, ImageDraw
import matplotlib



def analyze_music(file):

    # getting information from the file
    time_series, sample_rate = librosa.load(file)

    # getting a matrix which contains amplitude values according to frequency and time indexes
    # stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))
    stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=256))

    # converting the matrix to decibel matrix
    spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

    # transpose matrix; row is time stamp, column is frequency bin
    spectrogram = spectrogram.transpose()

    return spectrogram


def freq_per_timestamp(spect):

    avg_freq_ptime = []

    # for each time stamp
    for time in spect:

        index = 0
        avg_freq = 0
        intensity = 0

        # for each intensity of frequency bin
        for dB in time:
            intense = dB + 80

            avg_freq += index * int(intense)
            intensity += int(intense)
            index += 1

        try:

            avg_freq_ptime.append(int(avg_freq / intensity))

        except:
            avg_freq_ptime.append(-1)

    return avg_freq_ptime


def display(time):

    col_list = list(matplotlib.colors.cnames.values())  # get a list of colors
    col_list.append("#FFFFFF")  # white is put on end because that is default value

    w, h = len(time), 500

    img = Image.new("RGB", (w, h))

    img1 = ImageDraw.Draw(img)

    count = 0
    for col in time:
        count += 1

        shape = [(count, 500), (count, 0)]

        img1.line(shape, fill=col_list[col])


    img.show()
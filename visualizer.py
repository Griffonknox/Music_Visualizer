import librosa
from utils import analyze_music, freq_per_timestamp, display


if __name__ == "__main__":

    file = librosa.example('brahms')
    print(file)

    # file = "Alien.wav"
    spectro = analyze_music(file)

    time_line = freq_per_timestamp(spectro)

    display(time_line)

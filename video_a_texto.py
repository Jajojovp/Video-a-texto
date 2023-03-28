import youtube_dl
import speech_recognition as sr
import os
import librosa
import noisereduce as nr

def download_video_as_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def reduce_noise(audio_file):
    audio_data, sample_rate = librosa.load(audio_file, sr=None)
    reduced_noise = nr.reduce_noise(audio_clip=audio_data, noise_clip=audio_data, verbose=False)
    return reduced_noise, sample_rate


def transcribe_audio_to_text(audio_data, sample_rate):
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)

    try:
        text = recognizer.recognize_google(audio, language='es')
        return text
    except sr.UnknownValueError:
        print("Lo siento, no pude entender el audio.")
    except sr.RequestError as e:
        print(f"Error al llamar a la API de Google Speech Recognition; {e}")


if __name__ == "__main__":
    video_url = input("Por favor ingrese la URL del video de YouTube: ")
    download_video_as_audio(video_url)
    print("El audio ha sido extraído exitosamente.")

    audio_file = input("Por favor ingrese el nombre del archivo de audio extraído (incluida la extensión): ")

    if os.path.exists(audio_file):
        reduced_noise, sample_rate = reduce_noise(audio_file)
        text = transcribe_audio_to_text(reduced_noise, sample_rate)
        if text:
            print("Transcripción del audio:\n")
            print(text)
    else:
        print(f"No se encontró el archivo de audio {audio_file}.")

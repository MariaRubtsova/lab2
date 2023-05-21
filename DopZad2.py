from pydub import AudioSegment
def change_speed(file_path, speed):
    sound = AudioSegment.from_wav('Twenty_One_Pilots_-_Ride.wav')

    sound_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})

    new_file_path = f"{file_path}"
    sound_rate.export(new_file_path, format="wav")
    print(f"Файл успешно сохранен по пути {new_file_path}")


change_speed("song9.wav", 3)

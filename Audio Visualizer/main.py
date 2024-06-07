import pyaudio
import wave


class recorder(pyaudio.PyAudio):
    def __init__(self):
        super().__init__()

    def record(self, seconds, filename) -> wave.Wave_write:
        """Record a wav file for certain number of seconds. Save with the file name of filename"""

        stream = self.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

        frames = []

        for i in range(0, int(44100 / 1024 * seconds)):
            data = stream.read(1024)
            frames.append(data)

        # Stop Recording
        stream.stop_stream()
        stream.close()
        self.terminate()

        wave_file = wave.open(filename, 'wb')
        wave_file.setnchannels(1)
        wave_file.setsampwidth(self.get_sample_size(pyaudio.paInt16))
        wave_file.setframerate(44100)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

        return wave_file


def main() -> None:
    listener = recorder()

    listener.record(10, "new.wav")


if __name__ == "__main__":
    main()

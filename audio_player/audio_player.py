class AudioFile:
    def __init__(self, filename: str):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

    def play(self):
        raise NotImplementedError(
            "Must implement it's own play method"
        )  # Is it an interface? or abstract class?


class Mp3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"playing {self.filename} as mp3")


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print(f"playing {self.name} as wav")


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print(f"playing {self.filename} as ogg")


mp3file = Mp3File("testfile.mp3")
mp3file.play()

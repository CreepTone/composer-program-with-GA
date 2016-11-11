notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

class notecalc:
    def __init__(self, a):
        self.a = ord(a)
        self.a = self.a - 33
        self.octave = divmod(self.a, 12)[0]
        self.rest = divmod(self.a, 12)[1]
        if self.rest > 2:
            self.octave += 1
        self.note = notes[self.rest]
        self.note += str(self.octave)

    def AscToNote(self):
        return self.note

    def ReturnOct(self):
        return self.octave

    def ReturnNote(self):
        return self.rest

    def ReturnNote_abs(self):
        return self.a

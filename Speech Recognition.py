from vosk import Model, KaldiRecognizer
import pyaudio
import os
import time

model = Model("./Vosk/vosk-model-en-us-0.22-lgraph")

recogniser = KaldiRecognizer(model,16000)
mic = pyaudio.PyAudio()
stream = mic.open(rate = 16000,channels=1, format=pyaudio.paInt16,input= True,frames_per_buffer=8192)

def voice(seconds = 10):
    start_time = time.time()
   
    stream.start_stream()
    print("Model Started ....")
    
    while True:

        current_time = time.time()
        elapsed_time = current_time - start_time
        
        data = stream.read(4000,exception_on_overflow = False)
        recogniser.AcceptWaveform(data)

        result = recogniser.Result()[14:-3]
        print(result)

        if elapsed_time > seconds:
            break

voice()

    


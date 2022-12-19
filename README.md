# Offline Voice Control on Raspberry Pi.

### Designed To Run On:

* [Raspberry Pi](https://www.raspberrypi.org/).
* [Raspberry Pi OS](https://www.raspberrypi.com/software/).
* [Python 3](https://www.python.org/downloads/).

### The Voice Control Consists of:

* Speech-to-Text engine is a piece of software that interprets human voice into a string of text. It lets the computer know what is being said.
* Text-to-Speech engine converts text into sound. It allows the computer to speak, probably as a response to your command.

### The Voice Control uses:

* [Vosk](https://alphacephei.com/vosk/) as the Speech-to-Text engine.
* [PYTTSX3](https://pyttsx3.readthedocs.io/en/latest/) as the Text-to-Speech engine.

### Why Vosk ?

* Supports 20+ languages and dialects - English, Indian English, German, French, Spanish, Portuguese, Chinese, Russian, Turkish, Vietnamese, Italian, Dutch, Catalan, Arabic, Greek, Farsi, Filipino, Ukrainian, Kazakh, Swedish, Japanese, Esperanto, Hindi, Czech, Polish. More to come.
* Works offline, even on lightweight devices - Raspberry Pi, Android, iOS.
* Installs with simple `pip3 install vosk`.
* Portable per-language models are only 50Mb each, but there are much bigger server models available.
* Provides streaming API for the best user experience (unlike popular speech-recognition python packages).
* There are bindings for different programming languages, too - java/csharp/javascript etc.
* Allows quick reconfiguration of vocabulary for best accuracy.
* Supports speaker identification beside simple speech recognition.

### to use the Voice Control System you will need to:

- Speakers Plugged into the Raspberry Pi usingn Jack.
- Microphone Plugged ( Wired `USB` or Bluetooth ).

### Let's Get Started.

* First you need to install the necessary library packages which are:

  * pip install `pyaudio`.
  * pip install `vosk`.
  * pip install `pyttsx3`.

* or by using `pip install -r requirments.txt`

* After checking that the <a>Speaker</a> and <a>Microphone</a> works properly start using the Voice Control System using the Engine implementation.

## Speech To Text Engine:

Start using by importing Voice() which has seconds parameters that you can specity, ` default is 10 ` in your main application.

##### Code Implementation:
  
 ```python
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
 ```
 
## Text To Speech Engine:

Start using by importing speak() in your main application.

##### Code Implementation:
  
 ```python
 def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    print("Assistant : " + audio)
    engine.say(audio)
    engine.runAndWait()
```
`Note:  If you use the code in another python script you need to import these libraries.`

```python
import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio
import os
import time
```

It's that simple!

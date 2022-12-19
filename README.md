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

  * `pyaudio`
  * `vosk`
  

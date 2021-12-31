# Voice-assisstant
A personal voice assistant written in Python

Works with text-to-speech voices available for Windows 10.

## Check installed voices (optional)
By default Windows 10 comes with 2 voice packs, "David" and "Zira". The program can reference these by id: 0 is male, 1 is female. You may wany to install additional text-to-speech voice packs. If you do, this can change the voice index id, i.e.
- index -> 0 -- Microsoft David Desktop - English (United States)
- index -> 1 -- Microsoft Linda - English (Canada)
- index -> 2 -- Microsoft Susan - English (United Kingdom)
- index -> 3 -- Microsoft Heera - English (India)
- index -> 4 -- Microsoft Hazel Desktop - English (Great Britain)
- index -> 5 -- Microsoft Catherine - English (Australia)
- index -> 6 -- Microsoft Zira Desktop - English (United States)
The function check_voice_list() is included to verify which voice packs are installed and available for use, as well as their id's.

## Customization
You can set the properties below in your .env file to override the defaults:
```
voice_name = "Not Alexa"
voice_num = 1
city_name = "Your City"
```
Note: the voice recognition module can distinguish some names better than others.

## References & Inspiration
https://stackoverflow.com/questions/65573140/importerror-no-system-module-pywintypes-pywintypes39-dll
https://stackoverflow.com/questions/51992375/how-to-fix-installation-issues-for-pyaudio-portaudio-fatal-error-c1083-canno
https://stackoverflow.com/questions/62563668/how-to-make-voice-assistant-wait-for-a-command
https://pyttsx3.readthedocs.io/en/latest/engine.html#examples
https://windowsreport.com/unlock-new-text-to-speech-voice-windows-10/
https://support.microsoft.com/en-us/topic/download-voices-for-immersive-reader-read-mode-and-read-aloud-4c83a8d8-7486-42f7-8e46-2b0fdf753130
https://stackoverflow.com/questions/44858120/how-to-change-the-voice-in-pyttsx3
https://support.microsoft.com/en-us/topic/how-to-download-text-to-speech-languages-for-windows-10-d5a6b612-b3ae-423f-afa5-4f6caf1ec5d3
https://www.thewindowsclub.com/unlock-extra-text-to-speech-voices-in-windows
http://espeak.sourceforge.net/download.html
https://origin.geeksforgeeks.org/voice-assistant-using-python/
https://github.com/nateshmbhat/pyttsx3
https://pypi.org/project/python-weather/
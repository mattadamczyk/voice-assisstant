# Voice-assisstant
A personal voice assistant written in Python

## Check installed voices (optional)
Default for Windows 10: 0 is male, 1 is female
```
def check_voice_list():
    index = 0
    for voice in voices:
        print(f'index -> {index} -- {voice.name}')
        index +=1
check_voice_list()
```
If you install alternate voice packs, this list might be slightly different, i.e.
- index -> 0 -- Microsoft David Desktop - English (United States)
- index -> 1 -- Microsoft Linda - English (Canada)
- index -> 2 -- Microsoft Susan - English (United Kingdom)
- index -> 3 -- Microsoft Heera - English (India)
- index -> 4 -- Microsoft Hazel Desktop - English (Great Britain)
- index -> 5 -- Microsoft Catherine - English (Australia)
- index -> 6 -- Microsoft Zira Desktop - English (United States)

## Customization
### You could reference the voice names and id's from a dictionary
Note: the voice recognition module can distinguish some names better than others.
```
voices_dict = {0: 'David', 1: 'Linda', 2: 'Susan', 3: 'Heera', 4: 'Hazel', 5: 'Catherine', 6: 'Zira'}
voice_num = 4
voice_name = voices_dict[voice_num]
```

### Check or change voice rate
```
rate = engine.getProperty('rate')
engine.say('My current speaking rate is ' + str(rate))
```
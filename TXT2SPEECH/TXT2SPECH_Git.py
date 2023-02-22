#*** Python Text to Speech
import pyttsx3

# initialize Text-to-speech engine
TXT2SPCH_ENGINE = pyttsx3.init()
# convert this text to speech
text = ""
with open("input.txt", "r") as ipfile:
    data = ipfile.readlines()
    for line in data:
        text += line

# get details of all voices available
voices = TXT2SPCH_ENGINE.getProperty("voices")
#print(voices)

voiceCount = 0;
for voice in voices :
    print ("voice Count : ", voiceCount + 1)
    TXT2SPCH_ENGINE.setProperty("voice", voice.id)

    print("Spech at default rate : ", TXT2SPCH_ENGINE.getProperty("rate"))
    TXT2SPCH_ENGINE.say(text)
    TXT2SPCH_ENGINE.runAndWait()
    
    print("rate set to 300 : faster")
    TXT2SPCH_ENGINE.setProperty("rate", 300)
    TXT2SPCH_ENGINE.say(text)
    TXT2SPCH_ENGINE.runAndWait()
    
    print("rate set to 100 : slower")
    TXT2SPCH_ENGINE.setProperty("rate", 100)
    TXT2SPCH_ENGINE.say(text)
    TXT2SPCH_ENGINE.runAndWait()
    
    fileName = "audioSpeech" + str(voiceCount) + ".mp3"
    
    # play the speech
    #Setting the rate to default rate prior to saving to file
    TXT2SPCH_ENGINE.setProperty("rate", 200)
    TXT2SPCH_ENGINE.save_to_file(text, fileName)
    TXT2SPCH_ENGINE.runAndWait()
    
    voiceCount = voiceCount + 1

#coding=utf-8
import time
import pyaudio
import wave
def playAlarm():
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open("church.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()
alarmtime=(2017,11,13, 7, 30, 0, 6,  316, 0)
alarm=time.struct_time(alarmtime)
while(alarm!=time.localtime()):
    pass
playAlarm()

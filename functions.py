import thinkdsp
import random
import matplotlib.pyplot as plt
from track import *
from pydub import AudioSegment
from pydub.playback import play



# initialize list
seg_track1 = []
seg_track2 = [] 
two_bit = []
wave1 = []
to_mp3 = []


# beats
bt = 1.5


freq_list = {
    'C0':16.35, 'Db0':17.32,'D0':18.35,'Eb0':19.45,'E0':20.6,'F0':21.83,'Gb0':23.12,\
    'G0':24.5,'Ab0':25.96,'A0':27.5,'Bb0':29.14,'B0':30.87,'C1':32.7,'Db1':34.65,'D1':36.71,\
    'Eb1':38.89,'E1':41.2,'F1':43.65,'Gb1':46.25,'G1':49,'Ab1':51.91,'A1':55,'Bb1':58.27,\
    'B1':61.74,'C2':65.41,'Db2':69.3,'D2':73.42,'Eb2':77.78,'E2':82.41,'F2':87.31,'Gb2':92.5,\
    'G2':98,'Ab2':103.83,'A2':110,'Bb2':116.54,'B2':123.47,'C3':130.81,'Db3':138.59,'D3':146.83,\
    'Eb3':155.56,'E3':164.81,'F3':174.61,'Gb3':185,'G3':196,'Ab3':207.65,'A3':220,'Bb3':233.08,\
    'B3':246.94,'C4':261.63,'Db4':277.18,'D4':293.66,'Eb4':311.13,'E4':329.63,'F4':349.23,\
    'Gb4':369.99,'G4':392,'Ab4':415.3,'A4':440,'Bb4':466.16,'B4':493.88,'C5':523.25,'Db5':554.37,\
    'D5':587.33,'Eb5':622.25,'E5':659.25,'F5':698.46,'Gb5':739.99,'G5':783.99,'Ab5':830.61,'A5':880,\
    'Bb5':932.33,'B5':987.77,'C6':1046.5,'Db6':1108.73,'D6':1174.66,'Eb6':1244.51,'E6':1318.51,\
    'F6':1396.91,'Gb6':1479.98,'G6':1567.98,'Ab6':1661.22,'A6':1760,'Bb6':1864.66,'B6':1975.53,\
    'C7':2093,'Db7':2217.46,'D7':2349.32,'Eb7':2489.02,'E7':2637.02,'F7':2793.83,'Gb7':2959.96,\
    'G7':3135.96,'Ab7':3322.44,'A7':3520,'Bb7':3729.31,'B7':3951.07,'C8':4186.01,'Db':4434.92,\
    'D8':4698.63,'Eb8':4978.03,'E8':5274.04,'F8':5587.65,'Gb8':5919.91,'G8':6271.93,'Ab8':6644.88,\
    'A8':7040,'Bb8':7458.62,'B8':7902.13, 'rest':0
}


def make_note(Name="A4", amp=1.0, beats=1.0, filename="defaultFileName"):
    wave1.clear()
    
    # Initialize some values, let signal be empty first
    frequency = freq_list[Name]
    duration = beats / 2
    sin_sig = thinkdsp.SinSignal(freq=0)
    
    # Add overtones 
    for i in [x for x in range(0, 8) if x != 6]: 

        sin_sig += thinkdsp.SinSignal(freq=(frequency+(frequency*i)), amp=amp/(i+1), offset=0)
        # in mathematical expression sinsignal looks like this y = A sin(2πft + φ0)
        
        signal = thinkdsp.SinSignal(freq=(frequency+(frequency*i)), amp=amp/(i+1), offset=0)

        # different duration for plotting
        signal = signal.make_wave(duration=0.005, start=0, framerate=48000)
        wave1.append(signal)

    
    # Convert signal into wave to .wav file to audiosegment
    # 48000 standard sampling in recording studios, sampling rate = frame rate
    wave = sin_sig.make_wave(duration=duration, start=0, framerate=48000)
    final_wave = sin_sig.make_wave(duration=0.005, start=0, framerate=48000)
    wave1.append(final_wave)
    make_plot(name= Name)
    print(Name)

    wave.write(filename=filename)
    audio = AudioSegment.from_wav(filename)
    to_mp3.append(audio)
    return audio

# create plot
def make_plot(name):
    color = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink', 'black' ]
    plt.clf()
    for i in range(0, len(wave1)):
        plt.subplot(len(wave1), 1, (i+1))
        wave1[i].plot(color = color[i] )
        # Get a reference to the figure manager
    fig_manager = plt.get_current_fig_manager()

    # Set the window title of the plot
    fig_manager.set_window_title(name)
    plt.legend()
   
    plt.show()

# grouping the message into two bits
def groupBits(message):
    two_bit.clear()
    for i in range(0, len(message)-1, 2):
        bit = message[i:i+2]
        two_bit.append(bit)
    

# creating an array of audio segments      
def createseg(track, seg_track, digital_input):
    
    if (len(track)*2) != (len(digital_input)):
        for i in range((len(track)*2)-(len(digital_input))):
            digital_input+="1"
            
    groupBits(digital_input)
    for x in range(0, len(track)):
        print(len(two_bit))
        
# symbols to corres. decimal values
        if two_bit[x] == '00':
            beats = bt/4  
        elif two_bit[x] == '01':
            beats = bt/2
        elif two_bit[x] == '10':
            beats = bt
        elif two_bit[x] == '11':
            beats = bt*2
        else:
            beats = bt

# creating an array of audio segments          
        seg_track.append(make_note(track[x], beats=beats, amp = 1.0))
        print("Note:", track[x])
        print("sym:", two_bit[x], ":", beats)
#  make_plot(track)
    print(two_bit)
    
# mixing two tracks

def mixtracks(track1, track2, message1, message2):
# resets the list
 
    seg_track1.clear()
    seg_track2.clear()
    
    createseg(track1, seg_track1, message1)
    createseg(track2, seg_track2, message2)
    
    song = AudioSegment.empty()
    
    for i in range(len(track1)):
        note1 = seg_track1[i]
        note2 = seg_track2[i]
        song += note1[:len(note1)].overlay(note2[:len(note2)])

    return song
    
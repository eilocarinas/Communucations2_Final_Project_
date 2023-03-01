from functions import *

# storing the mixed tracks 
part1 = mixtracks(track1 = part1_note, track2 = part1_note_f, message1 = part1_message, message2= part1_message_long)
part2 = mixtracks(track1 = part2_note, track2 = part2_note_f, message1 = part2_message, message2= part2_message_long)
part3 = mixtracks(track1 = part3_note, track2 = part3_note_f, message1 = part3_message, message2= part3_message_long)


# arrays into one
song = part1 + part1+ part2 + part2 + part3 + part3
combined = AudioSegment.empty()

print("Playing:  Lupang Hinirang")

# plays the whole song

play(song) 

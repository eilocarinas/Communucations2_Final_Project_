from functions import *

part1 = mix2tracks(track1 = part1_note, track2 = part1_note_f, message1 = part1_message, message2= part1_message_long)
part2 = mix2tracks(track1 = part2_note, track2 = part2_note_f, message1 = part2_message, message2= part2_message_long)
part3 = mix2tracks(track1 = part3_note, track2 = part3_note_f, message1 = part3_message, message2= part3_message_long)
print("Playing:  Lupang Hinirang")
play(part1) #I
play(part1) #II
play(part2) #III
play(part2) #IV
play(part3) #V
play(part3) #VI
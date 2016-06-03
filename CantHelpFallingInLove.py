# CantHelpFallingInLove.py
# Sheet music from http://forpiano.com/FILEX/C/81ke8f2y89/elvis_presley--cant_help_fallin_in_love.pdf
 
from music import *
 
# Create the necessary musical data
cantHelpFallingInLoveScore = Score("Cant Help Falling In Love", 100.0)  # tempo is 108 bpm
 
pianoPart    = Part(PIANO, 0)        # strings part on channel 0
lyricsPart   = Part(RECORDER, 1)
 
melodyAPhrase = Phrase(0.0)            # theme starts at the beginning
melodyBPhrase = Phrase(0.0)
bassPhrase = Phrase(0.0)
lyricsPhrase = Phrase(0.0)

#Chorus measures

lyricsM1    = [F4, C5]
dlyricsM1   = [HN, HN]
melodyAM1   = [F4, C5]
dmelodyAM1  = [HN, HN]
melodyBM1   = [REST, C4, A3, F3, REST, A4, F4, C4]
dmelodyBM1  = [  EN, EN, EN, EN,   EN, EN, EN, EN]
bassM1      = [F2, A2]
dbassM1     = [HN, HN]

lyricsM2    = [F4, G4, A4]
dlyricsM2   = [HN, QN, QN]
melodyAM2   = [F4, REST, A3]
dmelodyAM2  = [HN,   QN, QN]
melodyBM2   = [REST, D4, A3, F3, REST, [E4,G4], [F4,A4]]
dmelodyBM2  = [  EN, EN, EN, EN,   QN,      EN,      EN]
bassM2     = [D2, D3, A2, F2, D2]
dbassM2    = [HN, EN, EN, EN, EN]

lyricsM3    = [B4, A4]
dlyricsM3   = [HN, HN]
melodyAM3   = [B4, REST, A4]
dmelodyAM3  = [HN,   QN, HN]
melodyBM3   = [REST, F4, D4, B3, REST, F4, C4, A4]
dmelodyBM3  = [  EN, EN, EN, EN,   EN, EN, EN, EN]
bassM3     = [B1, C2]
dbassM3    = [HN, HN]

lyricsM4    = [G4,  G4, C4]
dlyricsM4   = [HN, DQN, EN]
melodyAM4   = [G4,  G4, C4]
dmelodyAM4  = [HN, DQN, EN]
melodyBM4   = [REST, E4, C4, B3, REST, REST, [E3,B3]]
dmelodyBM4  = [  EN, EN, EN, EN,   QN,   EN,      EN]
bassM4     = [C2, G3, E3, D3, C3]
dbassM4    = [HN, EN, EN, EN, EN]

 #has not been fixed yet
 
lyricsM5    = [D4, E4]
dlyricsM5   = [HN, HN]
melodyAM5   = [D4, E4]
dmelodyAM5  = [HN, HN]
melodyBM5   = []
dmelodyBM5  = [EN, EN, EN, EN, EN, EN, EN, EN]
bassM5     = []
dbassM5    = [HN, HN]

# add the notes to the theme
melodyAPhrase.addNoteList(melodyAM1, dmelodyAM1)
melodyAPhrase.addNoteList(melodyAM2, dmelodyAM2)
melodyAPhrase.addNoteList(melodyAM3, dmelodyAM3)
melodyAPhrase.addNoteList(melodyAM4, dmelodyAM4)

melodyBPhrase.addNoteList(melodyBM1, dmelodyBM1)
melodyBPhrase.addNoteList(melodyBM2, dmelodyBM2)
melodyBPhrase.addNoteList(melodyBM4, dmelodyBM4)

bassPhrase.addNoteList(bassM1, dbassM1)
bassPhrase.addNoteList(bassM2, dbassM2)
bassPhrase.addNoteList(bassM3, dbassM3)
bassPhrase.addNoteList(bassM4, dbassM4)
#bassPhrase.addNoteList(bassM5, dbassM5)

lyricsPhrase.addNoteList(lyricsM1, dlyricsM1)
lyricsPhrase.addNoteList(lyricsM2, dlyricsM2)
lyricsPhrase.addNoteList(lyricsM3, dlyricsM3)
lyricsPhrase.addNoteList(lyricsM4, dlyricsM4)

# add phrases to corresponding parts
pianoPart.addPhrase(melodyAPhrase)
pianoPart.addPhrase(melodyBPhrase)
pianoPart.addPhrase(bassPhrase)
lyricsPart.addPhrase(lyricsPhrase)
 
# add parts to score
cantHelpFallingInLoveScore.addPart(pianoPart)
cantHelpFallingInLoveScore.addPart(lyricsPart)
 
# play score
Play.midi(cantHelpFallingInLoveScore)

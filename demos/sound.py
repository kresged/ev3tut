#!/usr/bin/micropython

# Note that we are using the generic micropython, which does not have Lego's pybricks Python module

from ev3dev2.sound import Sound

# Get a new sound object
snd = Sound()

# Speak
snd.speak("Let us have some star wars fun")

# Play a little song that was lifted from the ev3dev2 documentation.  The sequence of tones to play consists of a 3-tuple, where
# the first number is frequency in Hz, the second is duration in milliseconds, and the third is delay in milliseconds between
# this and the next tone in the sequence.
#
# Name that tune!  :-)
snd.tone([
    (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
    (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
    (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
    (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
    (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
    (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
    (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
    (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100),
    (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
    (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
    (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100),
    (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100), (392, 250, 100),
    (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
    (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
    (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
    (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200),
    (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
    (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
])

# Play a wav file -- there are lots of wav files stored below /usr/share/sounds/ev3dev on the EV3.
# Most likely, these are the sound files from Lego.
snd.play_file('/usr/share/sounds/ev3dev/communication/game_over.wav')

# Another example from the ev3dev2 documentation.  Somebody has too much time on their hands!
#
# Name this tune!
snd.play_song((
    ('D4', 'e3'),      # intro anacrouse
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),       # meas 1
    ('D5', 'h'),
    ('C5', 'e3'),      # meas 2
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),      # meas 3
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),      # meas 4
    ('B4', 'e3'),
    ('C5', 'e3'),
    ('A4', 'h.'),
))
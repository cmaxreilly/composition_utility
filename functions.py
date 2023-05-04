
def name_to_midi(pitch):
    # Dictionary mapping note names to MIDI note numbers
    note_dict = {'c': 0, 'c#': 1, 'd': 2, 'd#': 3, 'e': 4, 'f': 5, 'f#': 6, 'g': 7, 'g#': 8, 'a': 9, 'a#': 10, 'b': 11}
    # Parse the input pitch into note name and octave
    name, octave = pitch[:-1], int(pitch[-1])
    # Calculate the MIDI note number for the given pitch
    midi_note = 12 + note_dict[name.lower()] + (octave * 12)
    return midi_note


from midiutil.MidiFile import MIDIFile

def write_to_midi(pitches, filename):
    # Create a new MIDI file with one track
    midi_file = MIDIFile(1)
    track = 0
    
    # Set the tempo and time signature
    midi_file.addTempo(track, 0, 120)
    midi_file.addTimeSignature(track, 0, 4, 2)
    
    # Add the pitches as notes to the MIDI file
    time = 0
    volume = 100
    for pitch in pitches:
        pitch, duration = pitch.split(":")
        duration = int(duration)
        midi_file.addNote(track, 0, int(pitch), time, duration, volume)
        time += duration
    
    # Write the MIDI file to disk
    with open(filename, 'wb') as output_file:
        midi_file.writeFile(output_file)

def write_to_lilypond(pitches, filename):
    # Create the LilyPond input string
    input_string = "\\version \"2.20.0\"\n"
    input_string += "\\score {\n"
    input_string += "  \\new Staff {\n"
    input_string += "    \\time 4/4\n"
    input_string += "    \\relative c' {\n"
    
    # Convert each pitch to a LilyPond note with duration and add to the input string
    for pitch in pitches:
        pitch, duration = pitch.split(":")
        duration = int(duration)
        note_name = "c"
        octave = 0
        while int(pitch) > 11:
            note_name = chr(ord(note_name) + 1)
            pitch = int(pitch) - 12
        if int(pitch) < 3:
            octave -= 1
        elif int(pitch) > 14:
            octave += 1
        note_name += "'" * octave
        if int(pitch) % 12 == 1 or int(pitch) % 12 == 6:
            note_name += "is"
        elif int(pitch) % 12 == 4 or int(pitch) % 12 == 9:
            note_name += "es"
        input_string += "      " + note_name + str(duration) + " "
    
    # Add the LilyPond footer to the input string
    input_string += "}\n"
    input_string += "}"
    
    # Write the input string to a file
    with open(filename, "w") as f:
        f.write(input_string)


def write_to_lilypond(pitches, filename):
    # Create the LilyPond input string
    input_string = "\\version \"2.20.0\"\n"
    input_string += "\\score {\n"
    input_string += "  \\new Staff {\n"
    input_string += "    \\relative c' {\n"
    
    # Convert each pitch to a LilyPond note and add to the input string
    for pitch in pitches:
        note_name = "c"
        octave = 0
        while pitch > 11:
            note_name = chr(ord(note_name) + 1)
            pitch -= 12
        if pitch < 3:
            octave -= 1
        elif pitch > 14:
            octave += 1
        note_name += "'" * octave
        if pitch % 12 == 1 or pitch % 12 == 6:
            note_name += "is"
        elif pitch % 12 == 4 or pitch % 12 == 9:
            note_name += "es"
        input_string += "      " + note_name + " "
    
    # Add the LilyPond footer to the input string
    input_string += "}\n"
    input_string += "}"
    
    # Write the input string to a file
    with open(filename, "w") as f:
        f.write(input_string)


from midiutil.MidiFile import MIDIFile

def write_to_midi(pitches, filename):
    # Create a new MIDI file with one track
    midi_file = MIDIFile(1)
    track = 0
    
    # Set the tempo and time signature
    midi_file.addTempo(track, 0, 120)
    midi_file.addTimeSignature(track, 0, 4, 2)
    
    # Add the pitches as notes to the MIDI file
    time = 0
    duration = 1
    volume = 100
    for pitch in pitches:
        midi_file.addNote(track, 0, pitch, time, duration, volume)
        time += 1
    
    # Write the MIDI file to disk
    with open(filename, 'wb') as output_file:
        midi_file.writeFile(output_file)

def transpose_to_modes(motive):
    # Dictionary mapping mode names to their scale degrees
    modes_dict = {
        'Ionian': [0, 2, 4, 5, 7, 9, 11],
        'Dorian': [0, 2, 3, 5, 7, 9, 10],
        'Phrygian': [0, 1, 3, 5, 7, 8, 10],
        'Lydian': [0, 2, 4, 6, 7, 9, 11],
        'Mixolydian': [0, 2, 4, 5, 7, 9, 10],
        'Aeolian': [0, 2, 3, 5, 7, 8, 10],
        'Locrian': [0, 1, 3, 5, 6, 8, 10]
    }
    
    # Determine the pitch classes and intervals present in the input motive
    pc_set = set([note % 12 for note in motive])
    intervals = [(motive[i+1] - motive[i]) % 12 for i in range(len(motive)-1)]
    
    # Determine the possible modes using the pitch classes and intervals
    possible_modes = {}
    for mode, degrees in modes_dict.items():
        mode_pc_set = set([degree % 12 for degree in degrees])
        mode_intervals = [(degrees[i+1] - degrees[i]) % 12 for i in range(len(degrees)-1)]
        if pc_set.issubset(mode_pc_set) and set(intervals) == set(mode_intervals):
            transposed_motive = [(note - motive[0] + degrees[0]) % 12 + motive[0] for note in motive]
            possible_modes[mode] = transposed_motive
    
    return possible_modes


def transpose_to_modes(motive):
    # Dictionary mapping mode names to their scale degrees
    modes_dict = {
        'Ionian': [0, 2, 4, 5, 7, 9, 11],
        'Dorian': [0, 2, 3, 5, 7, 9, 10],
        'Phrygian': [0, 1, 3, 5, 7, 8, 10],
        'Lydian': [0, 2, 4, 6, 7, 9, 11],
        'Mixolydian': [0, 2, 4, 5, 7, 9, 10],
        'Aeolian': [0, 2, 3, 5, 7, 8, 10],
        'Locrian': [0, 1, 3, 5, 6, 8, 10]
    }
    
    # Determine the pitch classes present in the input motive
    pc_set = set([note % 12 for note in motive])
    
    # Determine the possible modes using the pitch classes
    possible_modes = {}
    for mode, degrees in modes_dict.items():
        mode_pc_set = set([degree % 12 for degree in degrees])
        if pc_set.issubset(mode_pc_set):
            transposed_motive = [(note - motive[0] + degrees[0]) % 12 + motive[0] for note in motive]
            possible_modes[mode] = transposed_motive
    
    return possible_modes

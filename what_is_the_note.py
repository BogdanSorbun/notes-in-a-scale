from itertools import cycle, islice

notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#','g', 'g#', 'a', 'a#', 'b']
names = ['do', 're', 'mi', 'fa', 'so', 'la', 'ti']
def note(scale, solfege):
    scale_index = notes.index(scale) + 1
    scale_semitones = [0, 2, 4, 5, 7, 9, 11]
    for index, semitone_location in enumerate(names):
        if semitone_location == solfege:
            i = scale_semitones[index]
    if solfege == 'do':
        return scale.capitalize()
    result = list(islice(cycle(notes), scale_index, i + scale_index))
    return result[-1].capitalize()
        
    
    
    

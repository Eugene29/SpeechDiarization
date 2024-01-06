from speaker_diarization import SpeakerDiarizer
from find_names import assign_speaker_name, transcript_to_dictionary
from pydub import AudioSegment

### INPUTS ###
audio_fname = "../data/Hinton.mp3"
num_speakers = 1
write_in_file = True ## if False, then it will just print.

print('Changing audio to mono channel')
stereo_audio = AudioSegment.from_file(audio_fname, format="mp3")
mono_audio = stereo_audio.set_channels(1)
mono_audio.export(audio_fname, format="mp3")

print("Initializing SpeakerDiarizer...")
diarizer = SpeakerDiarizer(num_speakers=num_speakers)
diarizer = SpeakerDiarizer()

print("Running diarization...")
transcript = diarizer.diarize(audio_fname)

print("Finished diarization. Transcript:", end='')
if write_in_file:
    print("Saved in text file")
    match = audio_fname.rfind('.')
    with open (audio_fname[:match]+'.txt', 'w') as file:
        file.write(transcript)
else:
    print(transcript)
    
print("Assigning Names:", end='')
try:
    fin_transcript = assign_speaker_name(transcript)
    print(fin_transcript)
    transcript_dictionary = transcript_to_dictionary(fin_transcript)
except TypeError:
    print("No names assigned due to unavailability")


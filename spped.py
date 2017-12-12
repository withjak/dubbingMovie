from pydub import AudioSegment


def speed_adjust(audio_name, desired_dur, current_dur):
    sound = AudioSegment.from_file(audio_name)

    # shift the pitch up by half an octave (speed will increase proportionally)
    octaves = 0.5

    new_sample_rate = int(sound.frame_rate * current_dur/desired_dur)

    # keep the same samples but tell the computer they ought to be played at the 
    # new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
    chipmunk_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

    # now we just convert it to a common sample rate (44.1k - standard audio CD) to 
    # make sure it works in regular audio players. Other than potentially losing audio quality (if
    # you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
    chipmunk_ready_to_export = chipmunk_sound.set_frame_rate(44100)

    chipmunk_ready_to_export.export('m.mp3', format='mp3')

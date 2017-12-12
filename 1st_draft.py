# Import everything needed to edit video clips
from moviepy.editor import *
import pysrt
from moviepy.editor import concatenate_audioclips
from tts_it import sub_to_audio
from speed import speed_adjust

# Load your movie
# Give proper path to your movie
videoclip = VideoFileClip("single_scene.mp4")
audioclip = videoclip.audio

#importing subtitles 
#provide full path to subtitle file
subs = pysrt.open('sub_1.srt')

# initializing some parameters
last_e = '00:00:00.00'
final_clip = audioclip.subclip(0,0)


def time_conv(_sub):
    ''' convert SubRipTime to usable format '''
    last_e_h, last_e_m, last_e_s, last_e_ms = _sub
    last_e_ms = last_e_ms//10
    s = str(last_e_h)+':'+str(last_e_m)+':'+str(last_e_s)+'.'+str(last_e_ms)
    return s


for sub in subs:

    s = time_conv(sub.start)
    e = time_conv(sub.end)

    _, __, d_m, d_s = sub.end - sub.start
    duration = int(d_m) + int(d_s)/1000 

    #music_clip = last_e --> sub.start
    #create music_clip
    music_clip = audioclip.subclip(last_e,s)
    
    #use sub to tts
    sub_to_audio(sub) 
    audioclip_robot = AudioFileClip("op.mp3")
    
    #adjust audioclip_robot duration
    speed_adjust("op.mp3", duration, audioclip_robot.duration)
    audioclip_robot_modified = AudioFileClip("m.mp3")
    
    # ... make some audio clips aclip1, aclip2, aclip3
    final_clip = concatenate_audioclips([final_clip, music_clip, audioclip_robot_modified])
    
    #update last_end
    last_e = e

# adding ending music
music_clip = audioclip.subclip(last_e)
final_clip = concatenate_audioclips([final_clip, music_clip])

# Write the result to a file (many options available !)
videoclip2 = videoclip.set_audio(final_clip)
videoclip2.write_videofile("my_edit.mp4")

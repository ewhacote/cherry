import re


def solution(m, musicinfos):
    answer, melody_len = "(None)", 0

    for musicinfo in musicinfos:
        start_time, end_time, music_name, music_melody = musicinfo.split(',')
        time = convert_time(end_time) - convert_time(start_time)
        memory, music = convert_melody(m), convert_melody(music_melody)
        q, r = divmod(time, len(music))
        music = music * q + music[:r]
        check = re.search(memory, music)

        if check and melody_len < len(music):
            answer, melody_len = music_name, len(music)

    return answer


def convert_time(time_str):
    hh, mm = map(int, time_str.split(':'))

    return hh * 60 + mm


def convert_melody(music_str):
    convert_table = {"C#": 'c', "D#": 'd', "F#": 'f', "G#": 'g', "A#": 'a'}
    for key, value in convert_table.items():
        music_str = re.sub(key, value, music_str)

    return music_str

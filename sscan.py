#!/usr/bin/python3
# scan.py
import os
import argparse
import ffprobe
from mutagen.mp3 import MP3
from pydub import AudioSegment

from correlation import correlate


def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i ", "--source-file", help="source file")
    parser.add_argument("-o ", "--target-file", help="target file")
    args = parser.parse_args()

    SOURCE_FILE = args.source_file if args.source_file else None
    TARGET_FILE = args.target_file if args.target_file else None
    if not SOURCE_FILE or not TARGET_FILE:
        raise Exception("Source or Target files not specified.")
    return SOURCE_FILE, TARGET_FILE


if __name__ == "__main__":
    SOURCE_FILE, TARGET_FILE = initialize()
    audio = MP3("nightt.mp3")
    maxLength = audio.info.length
    nStart = 0
    nEnd = 105
    song = AudioSegment.from_mp3(SOURCE_FILE)
    myList = []
    while nEnd < maxLength:
        current = song[nStart * 1000: nEnd * 1000]
        current.export("1.mp3")
        grade = correlate(TARGET_FILE, "1.mp3")
        os.remove("1.mp3")
        myList.append(grade)
        nStart = nEnd
        nEnd = nEnd + 105
    minVal = max(myList)
    minIndex = myList.index(minVal)
    minMinute = (minIndex * 105) // 60
    minSec = (minIndex * 105) % 60
    print("in time: " + str(minMinute) + ":"
          + str(minSec) + " a sample was found with certainty " + str(minVal * 100) + "%")

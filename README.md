# Simple tool to compare audio files
for more information note the master branch: kdave/audio-compare

you can use this code to scan for an audio samlple in other audio file.
determine the most likeable moment to an occurence of the sample within the long audio.
returns a window of 105 seconds (configurable in sscan.py) inside the long audio target file.

works for me with python 3.10, OS is WSL ubuntu

use: $ ./sscan.py -i file1.mp3 -o file2.mp3
    Calculating fingerprint by fpcalc for file1.mp3
    Calculating fingerprint by fpcalc for file3.mp3
    in time: 12:05: a sample was found with certainty 54.324%

Internally the fingerprint is generated by `fpcalc -length 500`, cached
versions can be produced by `fpcalc-gen`.

Changes:

- port to python3
- print the similary as percents
- print input files on separate lines
- support precalculated fingerprint in `file.mp3.fpcalc`

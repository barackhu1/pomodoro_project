#!/usr/bin/env python3

from playsound import playsound
import sys

HELP = """countdown v0.1 by BurnitDown (barackhu1@gmail.com), 2023

Parameters:

-h                      this help
-p                      play the sound effect (for adjusting the volume)
<time>                  where time can be given in different formats, e.g.
                        60    -> 60 seconds
                        60s   -> 60 seconds
                        1m    -> 1 minute
                        1m10s -> 1 minute and 10 seconds
                        1h5m  -> 1 hour and 5 minutes"""


def main():
    try:
        if sys.argv[1] == "-h":
            print(HELP)
        elif sys.argv[1] == "-p":
            playsound("red sun in the sky.mp3")
        # TODO
    except KeyboardInterrupt:
        print("Kilépés")


##############################################################################

if __name__ == "__main__":
    main()

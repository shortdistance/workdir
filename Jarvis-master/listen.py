#!/usr/bin/env python

from jarvis import Jarvis

import logging
from jarvis.config import *
from jarvis.speech import sr, r, m

logger = logging.getLogger(__name__)


def run_transcription_loop():
    r.operation_timeout = 5

    try:
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY, language=my_language)
                # value =  r.recognize_sphinx(audio)
                Jarvis.handle_action(value)
            except sr.UnknownValueError:
                print "Oops! Unknown Value Error"
            except sr.RequestError as e:
                print "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e)
            except sr.HTTPError:
                print "Oops! Http Error"
            except sr.URLError:
                print "Oops! URL Error"
            except sr.WaitTimeoutError:
                print "Oops! Wait Time Error"
            except Exception, e:
                print "Oops!" + e.message.capitalize()
    except KeyboardInterrupt:
        pass


def main():
    # Set up logger.
    FORMAT = '%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    run_transcription_loop()


if __name__ == '__main__':
    main()

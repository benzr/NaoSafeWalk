"""
  NaoSafeWalk : NAO (lebleu) is trying to move safely and to say hello to
   peope on its path
"""
from naoqi import ALproxy
import time
import sys
tts = ALProxy("ALTextToSpeech", "192.168.100.103", 9559)

txtFile="say.txt"
if len(sys.argv) > 1:
    txtFile = sys.argv[1]

fp = open(txtFile,"r")
for l in fp.readlines():
    print l
    tts.say(l)
    time.sleep(0.2)
fp.close()


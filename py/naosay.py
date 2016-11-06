"""
  NaoSafeWalk : NAO (lebleu) is trying to move safely and to say hello to
   peope on its path
"""
from naoqi import ALProxy
import time
import sys
import argparse

def sayHello(robotIp,robotPort):
    tts = ALProxy("ALTextToSpeech", robotIp, robotPort)
    tts.say("Bonjour")

def sayTxt(robotIp,robotPort,txtFile):
    tts = ALProxy("ALTextToSpeech", robotIp, robotPort)
    fp = open(txtFile,"r")
    for l in fp.readlines():
        print l
        tts.say(l)
        time.sleep(0.25)
    fp.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--text", type=str,
                        default="../resources/say_intro.txt",
                        help="text file to be said")
    args = parser.parse_args()
    sayTxt(args.ip, args.port,args.text)

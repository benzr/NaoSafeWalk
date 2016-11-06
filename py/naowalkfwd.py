"""
  NaoSafeWalk : NAO (lebleu) is trying to move safely and to say hello to
   peope on its path
"""
from naoqi import ALProxy
import time
import sys
import argparse

motionPxy = None

def init(robotIp,robotPort):
    global motionPxy
    motionPxy = ALProxy("ALMotion", robotIp, robotPort)

def moveFowardInfinite(speed):
    global motionPxy
    motionPxy.move(0.1,0.0,0.0) 

def moveFowardAndStop(speed,duration):
    global motionPxy
    motionPxy.move(0.1,0.0,0.0) 
    time.sleep(duration)
    motionPxy.move(0.0,0.0,0.0) 

def stop():
    global motionPxy
    motionPxy.move(0.0,0.0,0.0) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--vx", type=float,
                        default=0.1,
                        help="forward speed in m/s")
    parser.add_argument("--dur", type=float,
                        default=2.0,
                        help="duration in s")
    args = parser.parse_args()
    
    init(args.ip, args.port)
    moveForwardInfinite(args.vx)
    time.sleep(5.0)
    stop()

    moveForwardAndStop(args.vx,args.dur)


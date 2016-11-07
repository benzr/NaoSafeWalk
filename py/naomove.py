"""
  NaoSafeWalk : NAO (lebleu) is trying to move safely
"""
from naoqi import ALProxy
import time
import sys
import argparse

def move(robotIp, robotPort, x, y, theta, temps):
    try:
        motionProxy = ALProxy("ALMotion", robotIp, robotPort)
    except Exception,e:
        print "Could not create proxy to ALMotion"
        print "Error was: ",e
        sys.exit(1)

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIp, robotPort)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    postureProxy.goToPosture("StandInit", 0.5)

    frequency  = 1.0
    motionProxy.setWalkTargetVelocity(x, y, theta, frequency)

    time.sleep(temps)
    motionProxy.stopMove()
    postureProxy.goToPosture("StandInit", 0.0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--x", type=float, default=0.5,
                        help="Robot port number")
    parser.add_argument("--y", type=float, default=0.0,
                        help="Robot port number")
    parser.add_argument("--theta", type=float, default=0.0,
                        help="Robot port number")
    parser.add_argument("--time", type=float, default=2.0,
                        help="Robot port number")
    args = parser.parse_args()
    move(args.ip, args.port,args.x,args.y,args.theta,args.temps)
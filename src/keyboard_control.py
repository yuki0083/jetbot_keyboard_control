#!/usr/bin/env python

import rospy
from std_msgs.msg import String 

info="""
------------------
Moving around:
        i    
   j    k    l
        ,    
------------------
"""

def keyboard_control():
    rospy.init_node('keyboard_control')
    pub =rospy.Publisher('/jetbot_motors/cmd_str', String, queue_size=1)
    
    rate = rospy.Rate(50)
    print(info)
    msg = String()
    while not rospy.is_shutdown():
        key = raw_input()
        if key == 'i':
            msg.data = 'forward'
        elif key == 'k':
            msg.data = 'stop'
        elif key == 'j':
            msg.data = 'left'
        elif key == 'l':
            msg.data = 'right'
        elif key == ',':
            msg.data = 'backward'
        else:
            print("Input i,k,j,l,,")

        pub.publish(msg)
        msg.data = ""
        rate.sleep()

if __name__ == "__main__" :
    keyboard_control() 

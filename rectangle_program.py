import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
from clover.srv import SetLEDEffect

rospy.init_node('flight')

set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)



def navigate_wait(x=0, y=0, z=0, yaw=float('nan'), speed=0.5, frame_id='', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

set_effect(effect='blink', r=0, g=255, b=0)
navigate_wait(x=0, y=0, z=1, frame_id='body', auto_arm=True)
print(4)
set_effect(r=128, g=0, b=128)
navigate_wait(x=0, y=1.2, z=1, frame_id='aruco_map')
print(1)
set_effect(r=255, g=255, b=0)
navigate_wait(x=1.2, y=1.2, z=1, frame_id='aruco_map')
print(2)
set_effect(r=0, g=255, b=255)
navigate_wait(x=1.2, y=0, z=1, frame_id='aruco_map')
print(3)
set_effect(r=0, g=0, b=255)
navigate_wait(x=0, y=0, z=1, frame_id='aruco_map')
print(4)
set_effect(effect='rainbow')
land()

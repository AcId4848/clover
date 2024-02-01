# rostopic list
# rostopic echo /mavros/state
# rosservice list
# rosservice call /get telemetry "frame_id: 'aruco_map'"

# Model Editor
# /home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/clover_aruco.world

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_altitude = rospy.ServiceProxy('set_altitude', srv.SetAltitude)
set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
set_yaw_rate = rospy.ServiceProxy('set_yaw_rate', srv.SetYawRate)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

navigate(z=1.5, speed=0.5, frame='body', auto_arm=True)
rospy.sleep(3)
navigate(x=1, y=0, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
navigate(x=1, y=2, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
navigate(x=2, y=2, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
navigate(x=0, y=2, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
navigate(x=3, y=0, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
navigate(x=3, y=2, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
navigate(x=4, y=2, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
navigate(x=4, y=0, z=1, speed=1, frame='aruco_map')
rospy.sleep(3)
land()

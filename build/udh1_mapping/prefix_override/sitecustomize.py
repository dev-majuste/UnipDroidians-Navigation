import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/majuste/Programação/ROS2/UDH1/Navigation/install/udh1_mapping'

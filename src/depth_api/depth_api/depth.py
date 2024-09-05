import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class DepthSubscriber(Node):

    def __init__(self):
        super().__init__('depth_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/camera/depth/image_raw',
            self.listener_callback,
            10)
        self.bridge = CvBridge()

        
        self.point_x = 320 
        self.point_y = 240 

    def listener_callback(self, data):
        
        depth_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
        
        depth_value = depth_image[self.point_y, self.point_x]
        
        self.get_logger().info(f'Depth at point ({self.point_x}, {self.point_y}): {depth_value} mm')

def main(args=None):
    rclpy.init(args=args)

    depth_subscriber = DepthSubscriber()

    rclpy.spin(depth_subscriber)

    depth_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

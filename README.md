# depth_example

This repository demonstrates how to get depth information from a depth camera.

## Prerequisites
To get started, use the [pros_dabai_camera](https://github.com/screamlab/pros_dabai_camera)to set up your camera.

## Setup

1. Install Dependencies
    Make sure you have the necessary dependencies installed. Follow the instructions in the [pros_dabai_camera](https://github.com/screamlab/pros_dabai_camera) repository to set up the camera.

2. Start the Camera
    Use the following command to start the camera:
    
    ```
    ./run.sh
    ```

## Usage
The example code is designed to retrieve depth information from the camera. The depth value at the point (320, 240) will be logged.

Here is the code for subscribing to depth data:

```
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
```
## Notes
* Make sure that the depth camera is properly set up and running before executing the script.
* Adjust `self.point_x` and `self.point_y` if you need to get the depth value at a different point.
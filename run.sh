#!/bin/bash

DOCKER_IMAGE="ghcr.io/otischung/pros_ai_image:1.3.6"
DOCKER_NETWORK="scripts_my_bridge_network"

docker run -it --rm \
        --network $DOCKER_NETWORK \
        -v $(pwd)/src/depth_api:/workspaces/src/depth_api \
        $DOCKER_IMAGE \
        /bin/bash -c "source /workspaces/rebuild_colcon.rc && ros2 run depth_api depth_example"

# -*- coding: utf-8 -*-
import numpy as np
import time
from cv2 import imshow, waitKey, imwrite

import normalSpeed


def norm2bgr(norm):
    norm = ((norm + 1.0) * 127).astype("uint8")
    return norm


def depth2show(depth, norm_type='max'):
    show_depth = (depth / depth.max() * 256).astype("uint8")
    return show_depth


if __name__ == "__main__":
    fx = 1736.0597
    fy = 1740.7188

    k_size = 5
    distance_threshold = 2000
    difference_threshold = 20
    point_into_surface = False

    color = np.load("examplePicture/color.npy")
    depth = np.load("examplePicture/depth.npy")
    depth = depth.astype(np.uint16)

    t1 = time.time()
    """
    The coordinate of depth and normal is in cv coordinate:
        - x is horizontal
        - y is down (to align to the actual pixel coordinates used in digital images)
        - right-handed: positive z look-at direction
    """
    normals_map_out = normalSpeed.depth_normal(depth, fx, fy, k_size, distance_threshold, difference_threshold, point_into_surface)

    # If the normal point out the surface, the z of normal should be negetive.
    print("normals_map_out z mean:",  normals_map_out[:, :, 2].mean())
    # If the normal point into the surface, the z of normal should be positive, as z of depth.
    normals_map_in = normalSpeed.depth_normal(depth, fx, fy, k_size, distance_threshold, difference_threshold, True)
    print("normals_map_in z mean:",  normals_map_in[:, :, 2].mean())

    imshow('norm_out', norm2bgr(normals_map_out))
    imwrite("examplePicture/normal_out.jpg", norm2bgr(normals_map_out))

    imshow('norm_in', norm2bgr(normals_map_in))
    imwrite("examplePicture/normal_in.jpg", norm2bgr(normals_map_in))

    imshow('depth', depth2show(depth))
    imwrite('examplePicture/depth_view.jpg', depth2show(depth))

    cmd = waitKey(0)
    if cmd == ord('q'):
        exit()

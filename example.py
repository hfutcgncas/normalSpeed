# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/liujianran/.local/lib/python3.5/site-packages")

import numpy as np
import time
import cv2

import normalSpeed
import copy


if __name__ == "__main__":
    fx = 1736.0597
    fy = 1740.7188

    k_size = 5
    far_cut = 2000
    difference_threshold = 20
   
    color = np.load("examplePicture/color.npy")
    depth = np.load("examplePicture/depth.npy")
    depth = depth.astype(np.uint16)

    cv2.imshow('depth', 1.0*depth/np.max(depth))
    cv2.waitKey(0)

    normals_map = normalSpeed.depth_normal(depth, fx, fy, k_size, far_cut, near_cut)

    normals_map_bgr = normals_map[...,::-1]
    cv2.imshow('depth_n', normals_map_bgr)
    cv2.waitKey(0)
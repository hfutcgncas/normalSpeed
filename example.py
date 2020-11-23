# -*- coding: utf-8 -*-
import numpy as np
import time
import cv2
import normalSpeed


if __name__ == "__main__":
    fx = 1736.0597
    fy = 1740.7188

    k_size = 5
    distance_threshold = 2000
    difference_threshold = 20
   
    color = np.load("examplePicture/color.npy")
    depth = np.load("examplePicture/depth.npy")
    depth = depth.astype(np.uint16)
    
    t1 = time.time()
    normals_map = normalSpeed.depth_normal(depth, fx, fy, k_size, distance_threshold, difference_threshold)
    print("time used: ", time.time()-t1) 
    
    normals_map_bgr = normals_map[...,::-1] # rgb -> bgr
    cv2.imshow('depth', 1.0*depth/np.max(depth))
    cv2.waitKey(0)
    cv2.imshow('depth_n', normals_map_bgr)
    cv2.waitKey(0)

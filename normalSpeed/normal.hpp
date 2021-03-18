#ifndef _NORMAL_HPP_
#define _NORMAL_HPP_

#include <opencv2/core/core.hpp>
#include <opencv2/rgbd.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <vector>


void accumBilateral(long delta, long i, long j, long *A, long *b, int threshold);
cv::Mat depthNormals(const cv::Mat &src, float fx, float fy,  int kernel_size, int distance_threshold,
                             int difference_threshold, bool norm_point_into_face);
#endif

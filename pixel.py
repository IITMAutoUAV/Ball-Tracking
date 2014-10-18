// im2dots.cpp
// OpenCV code to achieve similar photo effect as shown in 
// http://photoshopessentials.com/photo-effects/color-dots/

#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

int main()
{
    cv::Mat src = cv::imread("image.jpg");
    if (!src.data)
        return -1;

    cv::Mat dst = cv::Mat::zeros(src.size(), CV_8UC3);
    cv::Mat cir = cv::Mat::zeros(src.size(), CV_8UC1);
    int bsize = 10;

    for (int i = 0; i < src.rows; i += bsize)
    {
        for (int j = 0; j < src.cols; j += bsize)
        {
            cv::Rect rect = cv::Rect(j, i, bsize, bsize) & 
                            cv::Rect(0, 0, src.cols, src.rows);

            cv::Mat sub_dst(dst, rect);
            sub_dst.setTo(cv::mean(src(rect)));

            cv::circle(
                cir, 
                cv::Point(j+bsize/2, i+bsize/2), 
                bsize/2-1, 
                CV_RGB(255,255,255), -1, CV_AA
            );
        }
    }

    cv::Mat cir_32f;
    cir.convertTo(cir_32f, CV_32F);
    cv::normalize(cir_32f, cir_32f, 0, 1, cv::NORM_MINMAX);

    cv::Mat dst_32f;
    dst.convertTo(dst_32f, CV_32F);

    std::vector<cv::Mat> channels;
    cv::split(dst_32f, channels);
    for (int i = 0; i < channels.size(); ++i)
        channels[i] = channels[i].mul(cir_32f);

    cv::merge(channels, dst_32f);
    dst_32f.convertTo(dst, CV_8U);

    cv::imshow("dst", dst);
    cv::waitKey();
    return 0;
}

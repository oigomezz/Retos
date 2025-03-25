# [Watching Video][link]

Assume you are watching a video on Youtube. Consider the following hypothetical model of how video buffering takes place.

The video renders d KB of data per second, if watched in decent quality. Since you have a 2G Net pack, the bandwidth is fluctuating and does not support smooth video buffer. Also, the data packets send by server each second are fluctuating. The browser accumulates the data packets in cache, and once it gathers at least d KB data, it will play one second of video and remove that data from cache. In case it does not have enough data in cache, it will pause video and wait for enough data packets to start rendering again.

Since you do not want to watch video with such breaks, you pause the video initially and wait for browser to get enough data so that you can watch video smoothly, till the end of video i.e with no breaks. Also, you don't have much time to spare, so you want to watch video as soon as possible.

There are N data packets in total, received at an interval of 1 second. Your browser receives Xi KB data in ith data packet. It takes 1 second to receive 1 data packet. Your job, now, is to decide the earliest possible time, from which you should start playing the video (i.e hit play button), so that you can enjoy it without any breaks, with decent quality.

Assume you can only play video in integral seconds of time i.e if cache has d / 2 KB data does not mean you can play 0.5 second video. Also, the total data sent by server will be an integral multiple of d.

## Input format

- The first line will contain two space separated integers, the value of N and d respectively.
- Next line will contain N space separated integers, the ith number representing the data quantity in KB received in ith data packet.

## Output format

Output in one line, an integer, denoting the minimum time after which you should start playing video.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/video-watching-8c6cbee6/

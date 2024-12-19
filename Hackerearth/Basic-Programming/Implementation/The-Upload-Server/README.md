# [The Upload Server][link]

A new website to host video and music is built up by the company X. The engineers at X are facing a major issue in identifying whether the data they receive in one of their API is of video or music.

Now, you will be given N lines of data. Each line of data consists a list of strings. Each string either represents an integer or a name. For each line of data, you need to check whether that data corresponds to a music or a video.

You need to follow the following rules to detect the data and store it:

1. A Music data consists of a name and an integer that denote the bitrate and nothing else.
2. A video data consists of a name and two integers that denote the resolution of the video and nothing else.
3. Rest of the data which does not match any of the formats above is to be ignored.
4. A music or a video name can consist of integers but it will contain at least one character of the English alphabets.
5. An integer in the data will consist only of integers, and it will never start with 0.

For each line of data, if it satisfies the constraints of a music then print M, if it satisfies constraints of a video print V, or else print N which means that the data has to be ignored.

## Input format

- The first line contains an integer N as input denoting the total numbers of lines in the input.
- Next N lines contains either two strings or three strings separated by space.

## Output format

For each data, you need to print either of the three characters N, V or M.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-upload-server-15bac95e/

# Group Photo

You and your friends want to take group photos. The process of taking photos can be described as follows:

On the photo, each photographed friend occupies a rectangle of pixels: the ith of them occupies the rectangle of width wi pixels and height hi pixels. On the group photo everybody stands in a line, thus the minimum pixel size of the photo including all the photographed friends, is W \* H, where W is the total sum of all widths and H is the maximum height among the heights of all the photographed friends.
The friends made n photos - the jth (1 <= j <= n) photo had everybody except for the jth friend as he was the photographer.
Print the minimum size of each made photo in pixels.

## Input format

- First line of the input will contain n denoting the number of students.
- Next n lines contain two integers each denoting wi and hi. First line of these n lines denotes the width and height occupied by first student, second corresponds to second student and so on.

## Output format

Print n space-separated numbers b1, b2, ..., bn, where bi — the total number of pixels on the minimum photo containing all friends expect for the ith one..

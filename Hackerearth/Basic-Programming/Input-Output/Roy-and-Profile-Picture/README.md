# [Roy and Profile Picture][link]

Roy wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload. Minimum dimension of the picture can be L x L, where L is the length of the side of square.

Now Roy has N photos of various dimensions. Dimension of a photo is denoted as W x H where W - width of the photo and H - Height of the photo.

When any photo is uploaded following events may occur

1. If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
2. If width and height, both are large enough and (a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case. (b) else user is prompted to crop it. Print "CROP IT" in this case.

(quotes are only for clarification)

Given L, N, W and H as input, print appropriate text as output.

## Input format

- First line contains L.
- Second line contains N, number of photos.
- Following N lines each contains two space separated integers W and H.

## Output format

Print appropriate text for each photo in a new line.

[link]: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

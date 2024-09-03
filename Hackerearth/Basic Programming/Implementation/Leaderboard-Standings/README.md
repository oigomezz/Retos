# Leaderboard Standings

There were N submissions made in a programming contest containing infinite problems. Each submission earned the contestant 100 points as none of the submissions is a wrong or a partial submission. You are given the details of the submissions - the username of the contestant and the time taken to solve the problem. Your task is to print the rank list according to the following rules:

1. The contestant with a higher score gets a higher rank.
2. If the scores are tied, then the contestant with the least sum of the time taken to solve the problems gets a higher rank.
3. In case of a tie in both scores and sum of the time taken, they are ranked lexicographically according to their usernames.

**Note:** The details of the submissions are not sorted in any order (neither by time nor by username)

## Input format

The first line of every test file contains an integer N, the number of submissions. N lines follow, each being the details of ith submission.

Each of the N lines contains a string Ci, the username of the contestant corresponding to ith submission, and an integer Ti, the time of submission in minutes, separated by a space.

## Output format

Output the rank of the contestant and the username, in the increasing order of the ranks. Each rank should be displayed in a newline.

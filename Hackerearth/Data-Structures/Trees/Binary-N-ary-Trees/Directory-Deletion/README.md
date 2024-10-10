# Directory Deletion

You are given a directory tree of N directories/folders. Each directory is represented by a particular id which ranges from 1 to N. The id of the root directory is 1, then it has some child directories, those directories may contain some other ones and it goes on. Now you are given a list of directory id's to delete, you need to find the minimum number of directories that need to be deleted so that all the directories in the given list get deleted.

**Note** that if you delete a particular directory, all its child directories will also get deleted.

## Input format

- The first line of input contains an integer N that denotes how many folders are there.
- The next line contains N space separated integers that where the i-th integer denotes the id of the parent of the directory with id i. Note that the first integer will be -1 as 1 is the id of root folder and it has no parent. Rest of the integers will not be -1.
- The next line contains an integer M that denotes how many directories you need to delete.
- The next line contains M space separated integers that denote the ids of the directories you need to delete.

## Output format

Print the minimum number of directories that need to be deleted.

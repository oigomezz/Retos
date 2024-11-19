# A website

On a website, there are M users and they want to change their names. You will be given M lines consisting of two strings A and B, where username A wants to change his username to B. But the website does not support multiple users with the same username that is No two users can have the same username at the same time. A user can change his username from his current name to any name (X) if there is no user named X.

Every change in the username costs 1 unit of money. Find minimum cost to achieve these changes.

Notes

- If user X wants to change his username from a to b while user Y wants to change his username from b to a neither of the users can directly change as if a changes his name to b now there will be two users having the username b.
- If user X wants to change his username from a to a, so the user doesn't need to do anything.
- It is guaranteed that no two users have the same username initially and no two users will have the same once all the changes are done.
- It can be proved that the changes can always be done.

## Input format

- The first line consists of an integer T denoting the number of test cases.
- The first line of each test case contains an integer M denoting the number of users.
- Each of the next M lines of every test case contain two strings A and B where the i-th user wants to change his username from A to B.

## Output format

For each test case print a single line denoting the minimum cost for completing the changes in usernames.

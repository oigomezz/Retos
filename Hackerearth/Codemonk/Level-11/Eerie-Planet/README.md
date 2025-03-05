# Eerie Planet

You own a club on eerie planet. The day on this planet comprises of H hours. You appointed C crew members to handle the huge crowd that you get, being the best club on the planet. Each member of the crew has fixed number of duty hours to work. There can be multiple or no crew members at work at any given hour of the day.

Being on weird planet, the rules of this club cannot be normal. Each member of the crew only allows people who are taller than him to enter the club when he is at work.

Given the schedule of work and heights of the crew members, you have to answer Q queries. Each query specifies the time of entry and height of a person who is visiting the club. You have to answer if the person will be allowed to enter the club or not.

## Input format

- First line of the input contains 3 integers, H,C,Q. Representing number of hours in a day, number of crew members and number of queries respectively.
- Next C lines follow, where each line contains 3 integers, hi, Si, Ei, representing height of the crew member and start and end hour of his/her work schedule. He/she works for hours [Si, Ei], both inclusive.
- Next Q lines follow, each containing 2 integers, hi, ti, representing height and time (in hour) of the person trying to enter the club.

## Output format

Q lines, each line containing "YES" or "NO", without the quotes, answering if the person will be allowed to enter the club or not.

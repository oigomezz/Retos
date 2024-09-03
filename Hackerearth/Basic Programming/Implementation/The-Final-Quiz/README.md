# The Final Quiz

You, Bob and Alice are playing a quizzing game. Throughout the game you and the other two competitors have gained some points. Now at the end of the game, the three of you are given a final question. Before you hear the question you have to guess some special points.

If a contestant answers the question correctly he/she will be awarded the points equal to the special points he guessed and the same amount of points (he guessed ) will be deducted in case of a wrong answer. The participant who ends up with highest score after the final question will end up winning the game.

Now it is time for you to guess your special points. You can bet any amount between 0 and your current score , both inclusive. You are given your current scoreX followed by the current scores of AliceY and BobZ . You are also given special points guessed by Alice A and special points guessed by Bob B. You have to guess your special points, which maximizes your probability of winning the Quiz.

You can assume that you and both the other participants each independently have a 50% chance to answer correctly. If multiple special points can give you the highest probability of winning, choose the minimum one.

## Input format

- First line : T i.e number of testcases.
- For each testcase :
  - First line : Three space separated integers X, Y and Z.
  - Second line : Two space separated integers A and B.

## Output format

Print the minimum guessed special points that maximizes your chance of winning.

# [Scheduling War][link]

Prateek and Chintu are working on different projects both with equal priority. They both need to run some batches of processes. A batch has processes which need some systems to run them irrespective of the number of process running on each dependent system. If a batch runs then the dependent systems are occupied by its processes. No system can run processes from different projects and thus a system can process only chintu's processes or prateek's processes. Their manager being a stylo creep has allowed prateek to run his batches. Chintu felt offended and complained the CTO directly due to which the manager came up with a condition that if chintu can increase the number of processes running in total by replacing some or all of prateeks processes then only he can run his batches. Chintu wants to maximize the total processes running in order to show the manager his skills. Help him complete his task.

## Note

- A system can run any number of process from multiple batches at the same time but only of Chintu or of Prateek.

- Prateek's processes are running on some or all systems. Now, chintu has to run his batches of processes inorder to increase the number of running processes across all systems. A batch of chintu either runs all its processes or doesn't run any of them.

- If Chintu has replaced a system with his own processes then another batch of him can run its processes on that system.

- A batch needs 's' systems and runs 'p' processes overall, in any manner.

## Input format

- The first line contains the total number of systems - 'n'.
- The next line contains 'n' space separated integers - 'Si', denoting the number of prateek's processes running on i-th system.
- Next line contains an integer - 'b' denoting the number of batches Chintu has.
- This is followed by each line containing space separated integers where the first integer is - 's', number of systems the i-th batch needs followed by 's' integers denoting the system numbers and then the number of processes - 'p', the batch needs to run.

## Output format

The increase in number of processes Chintu can put in by replacing some of all of prateeks processes from some or all systems.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/maximum-flow/practice-problems/algorithm/scheduling-war/

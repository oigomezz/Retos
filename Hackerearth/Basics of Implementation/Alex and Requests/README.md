# Alex and Requests

Alex is working in a firm, where he needs to process requests according to their priority. He has N allocation systems. At any instance, ith system can process only one request with priority i or above.

For each request, on any eligible system, Alex can also terminate the request with less priority than that of the current request, in order to assign the current request to the system. There will be Q incoming requests and he needs to tell whether he can assign a system to each request or not.

Alex needs to assign each request to the system optimally, such that he can assign maximum number of incoming requests. The number of requests (which are already assigned) terminated by Alex, doesn't matter here.

**Note:** If not terminated explicitly, consider the processing time of every request as infinite.

## Input format

- First line of the input contains N, denoting the number of allocation systems.
- Next line contains one integer Q, which denotes the number of incoming requests.
  - In next Q lines, each line contains one integer X, denoting the priority of the request.

## Output format

For each incoming request, in new line print YES, if Alex can assign a system to the request, else print NO.

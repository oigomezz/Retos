# [URL shortener][link]

You have a URL-shortening service that registered users can use to create custom short links for any website. The service can also be used through an API which has the following requirements:

- There is a rate limit of 5 seconds for every user, i.e, the user must wait for at least 5 seconds after using the service before using it again.
- The URL provided must begin with either http:// or https://.
- The custom key chosen must be between 2 and 12 characters long (inclusive), and consist of alphabets and numbers only.
- The custom key should not be taken already (the custom key must be unique).

If all the conditions are met, then the custom key is added to the database and it redirects to the given website. The database is empty before the first query and after that, the custom keys of successful queries are added to the database one by one.

You will be given a list of queries made to the API in chronological order. Determine whether each query is successful. Each query will contain the following:

- time: The epoch time at which the query was made.
- URL: The URL of the original website.
- key: The custom key.
- userId: An integer that identifies the particular user who made the query.

**Task** You are given N queries. If a query is successful, print "YES" else print "NO".

**Function description** Complete the function solve provided in the editor. This function takes the following 2 parameters and returns the required answer:

- N: Represents the number of queries
- queries: Represents a 2D array of N rows and 4 columns denoting the queries

## Input format

- The first line contains a single integer N, denoting the number of queries.
- Each of the next N lines contains 4 values - the time, URL, key, and user id for the corresponding query.

## Output format

For each query, print either "YES" or "NO" (case-sensitive) depending on whether the query is successful or not.

[link]: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/url-shortener-2-615de05d/

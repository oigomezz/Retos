# [Flight Search][link]

You work as a software developer for a major airline company. The company assigns you to develop a program for listing the available flight options from a city A to another city B. To benefit the passengers, you are requested to order the listing in price ascending order with the cheapest flight option on top.

If there are multiple flight options for the same price, the option with lesser connecting flights is ordered higher.In case there are multiple flight options with equal number of connecting flights for the same price, then they are ordered alphabetically.

To get from one city to another, a passenger has an option to take either a direct flight, if available, or a sequence of connecting flights

## Input format

- The first line of the input contains the two cities for whom the listing of flight options must be produced – the departure city and the arrival city, separated by a white-space. The city name will be no longer than 20 characters and will not contain any white-space characters.
- The next N lines will contain the available flights and their costs. Each line is a direct flight starting with the departure city name, followed by the arrival city name, and lastly followed by the cost of that flight (in Rupees) – all three separate by a white-space character.

## Output format

The output is a list of M lines. Each line is one option of the flight listing. Each of the M lines start with the departure city name, followed by a sequence of connecting city names (if exists), then followed by the arrival city name, and lastly followed by the total cost of that option. All of them separated by a white-space character.

If there are zero flight options available, the output contains a single line of text - No Flights

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/the-flight-optimization-0267b2b5/

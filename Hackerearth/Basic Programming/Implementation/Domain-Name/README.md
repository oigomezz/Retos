# Domain Name

A Domain name is a string that identifies a realm of administrative autonomy, authority, or control within the Internet. Domain names are often used to identify services provided through the Internet, such as websites, email services, and more. As of 2017, 330.6 million domain names had been registered. Domain names are used in various networking contexts and for application-specific naming and addressing purposes. In general, a domain name identifies a network domain or an Internet Protocol (IP) resource, such as a personal computer used to access the Internet, or a server computer.

A Fully Qualified Domain Name (FQDN), sometimes also referred to as an absolute domain name, is a domain name that specifies its exact location in the tree hierarchy of the DNS (Domain Name System). It specifies all domain levels, including the top-level domain and the root zone. A fully qualified domain name is distinguished by its lack of ambiguity in terms of DNS zone location in the hierarchy of DNS labels: it can be interpreted only in one way.

A fully qualified domain name is conventionally written as a list of domain labels separated using the full stop “.” character (dot or period). The top of the hierarchy in an FQDN begins with the rightmost label. For instance, in the FQDN somehost.example.com, com is a label directly under the root zone,  example is nested under com, and finally somehost is nested under example.com.

The topmost layer of every domain name is the DNS root zone (TLD), which is expressed as an empty label and can be represented in an FQDN with a trailing dot, such as somehost.example.com.. A trailing dot is generally implied and often omitted by most applications. Trailing dots are required by the standard format for DNS zone files as well as to disambiguate cases where an FQDN does not contain any other label separators, such as the FQDNs for the root zone itself and any top-level domain.

The length of each label must be between 1 and 63 octets, and the full domain name is limited to 255 octets, full stops included.

**Task** Check if the given string forms a valid Fully Qualified Domain name.

**Assumptions** Hostnames are composed of a series of labels concatenated with dots. Each label is 1 to 63 characters long, and may contain:

- The ASCII letters a-z (in a case-insensitive manner),
- Digits 0-9
- Hyphen ('-').

Additionally

- Labels cannot start or end with hyphens
- Labels can start with numbers
- Max length of ASCII hostname including dots is 253 characters (not counting trailing dots)
- Underscores are not allowed in hostnames (but are allowed in other DNS types)

Some more assumptions are:

- TLD is at least 2 characters and only a-z
- We want at least 1 level above TLD
- No trailing dots after TLD

## Input format

**Note** This is the input format you must use to provide custom input (available above the Compile and Test buttons).

The first line contains T denoting the number of test cases.

Followed by T Lines :

- Each T line contains a String denoting the Full Domain name.

## Output format

For each test case in a new line, print either true for Valid or false for Invalid

canonical-gmail
===============

When evaluating the addresses of incoming mail, Gmail servers...
- Are case insensitive
- Ignore periods
- Ignore any text after a plus sign

Additionally, and @gmail.com  @googlemail.com can be used interchangeably.

So...

EXAMPLE+foo@gmail.com == example+bar@gmail.com == exam.ple@googlemail.com

All of these variables make it difficult to check a given email address for uniqueness.

This normalize(email) method in this module transforms any email address on a Gmail server to its 
canonical representation  (E.g., Example.Test+foo@googlemail.com becomes exampletest@gmail.com) 
so that it can be compared against other canonical addresses.

The canonical address should not be stored in lieu of the user's inputed address, as some
folks use the plus sign "hack" to route their incoming email to particular folders. These
Gmail power users can be a persnickety bunch. Don't mess up their system.

DEPENDENCY: https://github.com/rthalley/dnspython (or 'pip install dnspython')

canonical_gmail.py
===============

When evaluating the addresses of incoming mail, Gmail servers...
- Are case insensitive
- Ignore periods
- Ignore any text after a plus sign

Additionally, @gmail.com and @googlemail.com can be used interchangeably.

So...

example@gmail.com == EXAMPLE+foo@gmail.com == example+bar@gmail.com == exam.ple@googlemail.com

All of these variables make it difficult to check a given email address for uniqueness.

The normalize(email) method in canonical_gmail.py transforms any email address on a Gmail server, 
including Google Apps addresses with custom domains, to its simplest, canonical representation  
(E.g., exam.ple+foo@googlemail.com becomes example@gmail.com) so that it can be compared 
against other canonical addresses.

**The canonical address should not be stored in lieu of the user's inputed address**, as some
folks use these modifications to route their incoming email to particular folders.These Gmail 
power users can be a persnickety bunch. Don't mess up their system.

DEPENDENCY: https://github.com/rthalley/dnspython (or 'pip install dnspython')

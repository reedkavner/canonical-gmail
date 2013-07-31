'''
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
'''

import dns.resolver

#This function takes an email address and returns it's canonical representation
def normalize(email):
    try:
        email = email.lower()
        user, server = email.split('@')
        domain, tld = server.split('.', 1)
    except:
        #if there's an exception here it was probably not a valid email address
        return None
   
    if domain == 'googlemail':
        domain = 'gmail'
    
    if is_gmail_server(domain, tld) == True:
        user = user.split('+')[0].replace('.', '')
    
    normalized_email = user + '@' + domain + '.' + tld
    
    return normalized_email

#This function evaluates whether or not an email address resides on a Gmail server
def is_gmail_server(domain, tld):
    if domain == 'gmail':
        is_gmail = True
    
    else:
        is_gmail = False
        for i in dns.resolver.query(domain+'.'+tld, 'MX'):
            if "ASPMX.L.GOOGLE.COM" in i.to_text().upper():
                is_gmail = True
                break

    return is_gmail
    
    
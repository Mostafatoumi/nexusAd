# nexusAD Tool

I created this tool for fun and learning purposes. If you're interested in the development process and want to learn more, visit my main blog [here](https://mostafatoumi.github.io/).

## Installation

To install the required dependencies, run:

```bash
pip3 install -r requirements.txt
```
## How to use this simple tool ?

Simply run the command `python3 nexusAD.py -h` to see the available functionalities of this tool :


```bash
┌──(root㉿emsec)-[/opt/nexusAd]
└─# python3 nexusAD.py -h
usage: nexusAD.py [-h] -domain DOMAIN -u USERNAME -p PASSWORD -dc DOMAIN_CONTROLLER -sf SEARCH_FILTER [-add-user ADD_USER] [-add-group ADD_GROUP] [-add-ou ADD_OU]
                  [-modify-object MODIFY_OBJECT] [-delete-object DELETE_OBJECT]

LDAP Tool

options:
  -h, --help            show this help message and exit
  -domain DOMAIN        Domain name, e.g., example.com
  -u USERNAME, --username USERNAME
                        Username
  -p PASSWORD, --password PASSWORD
                        Password
  -dc DOMAIN_CONTROLLER, --domain-controller DOMAIN_CONTROLLER
                        Domain Controller IP
  -sf SEARCH_FILTER, --search-filter SEARCH_FILTER
                        Specify the LDAP search filter. For example, '(&(objectClass=user)(sAMAccountName=jdoe))'.
  -add-user ADD_USER    Add a new user
  -add-group ADD_GROUP  Add a new group
  -add-ou ADD_OU        Add a new Organizational Unit (OU)
  -modify-object MODIFY_OBJECT
                        Modify an LDAP object
  -delete-object DELETE_OBJECT
                        Delete an object, e.g., CN=emsec,CN=users,DC=example,DC=com

```
***Note: The `-modify-object` option is not currently functional. Consider it a next step to implement this feature in your tool. As mentioned before, this tool was created just for fun and learning purposes.***

## Tool Options :

* add user :

```bash
┌──(root㉿emsec)-[/opt/nexusAd]
└─# python3 nexusAD.py -domain emsec.htb -u admin -p Password@123! -dc 10.10.10.10 -add-user fun_user
[*] Successfully connected to LDAP server at ldap://10.10.10.10

[+] User fun_user added successfully.

User Path : cn=fun_user,cn=users,dc=emsec,dc=htb
```

* add group :

```bash
┌──(root㉿emsec)-[/opt/nexusAd]
└─# python3 nexusAD.py -domain emsec.htb -u admin -p Password@123! -dc 10.10.10.10  -add-group fun_group
[*] Successfully connected to LDAP server at ldap://10.10.10.10

[+] Group fun_group added successfully.

User Path : cn=fun_group,cn=users,dc=emsec,dc=htb
```

* add organizational unit :

```bash
┌──(root㉿emsec)-[/opt/nexusAd]
└─# python3 nexusAD.py -domain emsec.htb -u admin -p Password@123! -dc 10.10.10.10  -add-ou fun_ou
[*] Successfully connected to LDAP server at ldap://10.10.10.10

ou=fun_ou,dc=emsec,dc=htb
[*] Creatr OU :

[+] Ou fun_ou added successfully.

Ou Path : ou=fun_ou,dc=emsec,dc=htb
```


*  dump all users :

```bash
┌──(root㉿emsec)-[/opt/nexusAd]
└─# python3 nexusAD.py -domain emsec.htb -u admin -p Password@123! -dc 10.10.10.10 -sf '(objectclass=person)'
[*] Successfully connected to LDAP server at ldap://10.10.10.10

[*] Search results for filter '(objectclass=person)': 

[*] DN: CN=Administrator,CN=Users,DC=emsec,DC=htb     
[*] DN: CN=Guest,CN=Users,DC=emsec,DC=htb
[*] DN: CN=EMSEC,OU=Domain Controllers,DC=emsec,DC=htb
[*] DN: CN=krbtgt,CN=Users,DC=emsec,DC=htb
[*] DN: CN=Amanda Walker,CN=Users,DC=emsec,DC=htb     
[*] DN: CN=winrm_svc,CN=Users,DC=emsec,DC=htb
[*] DN: CN=user1,CN=Users,DC=emsec,DC=htb
[*] DN: CN=user2,CN=Users,DC=emsec,DC=htb
[*] DN: CN=user3,CN=Users,DC=emsec,DC=htb
[*] DN: CN=user4,CN=Users,DC=emsec,DC=htb
[*] DN: CN=Renamed_User,OU=LDAP3_OU,DC=emsec,DC=htb
[*] DN: CN=lol,OU=LDAP3_OU,DC=emsec,DC=htb
[*] DN: CN=user9,CN=Users,DC=emsec,DC=htb
[*] DN: CN=user10,CN=Users,DC=emsec,DC=htb
[*] DN: CN=admin,CN=Users,DC=emsec,DC=htb
[*] DN: CN=user11,CN=Users,DC=emsec,DC=htb
[*] DN: CN=fun_user,CN=Users,DC=emsec,DC=htb
```

* dump all group :

```bash
┌──(root㉿emsec)-[/opt/nexusAd]
└─# python3 nexusAD.py -domain emsec.htb -u admin -p Password@123! -dc 10.10.10.10 -sf '(objectclass=group)' 
[*] Successfully connected to LDAP server at ldap://10.10.10.10

[*] Search results for filter '(objectclass=group)':

[*] DN: CN=Administrators,CN=Builtin,DC=emsec,DC=htb
[*] DN: CN=RAS and IAS Servers,CN=Users,DC=emsec,DC=htb
[*] DN: CN=Server Operators,CN=Builtin,DC=emsec,DC=htb
[*] DN: CN=Account Operators,CN=Builtin,DC=emsec,DC=htb
[*] DN: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=emsec,DC=htb
[*] DN: CN=Cloneable Domain Controllers,CN=Users,DC=emsec,DC=htb
[*] DN: CN=Protected Users,CN=Users,DC=emsec,DC=htb
[*] DN: CN=Key Admins,CN=Users,DC=emsec,DC=htb
[*] DN: CN=Enterprise Key Admins,CN=Users,DC=emsec,DC=htb
[*] DN: CN=DnsAdmins,CN=Users,DC=emsec,DC=htb
[*] DN: CN=DnsUpdateProxy,CN=Users,DC=emsec,DC=htb
[*] DN: CN=Test_Group,OU=LDAP3_OU,DC=emsec,DC=htb
[*] DN: CN=fun_group,CN=Users,DC=emsec,DC=htb
```


* delete objects :

```bash
┌──(root㉿emsec)-[/opt/nexusAd]
└─# python3 nexusAD.py -domain emsec.htb -u admin -p Password@123! -dc 10.10.10.10  -delete-object CN=fun_user,CN=Users,DC=emsec,DC=htb
[*] Successfully connected to LDAP server at ldap://10.10.10.10

[+] Object CN=fun_user,CN=Users,DC=emsec,DC=htb deleted successfully.

```

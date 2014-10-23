Router_Control
==============

Control an TL-SG2008 Smart Switch via Telnet (for ACL Binding)

This is the first steps towards an Python script for controlling the SG2008, and similar switches from TP-Link.

This script will telnet into the router, and enable or disable an ACL Policy, as defined on the command line.

For example:

python router_test.py -u HAUser -p 12345678 -r 192.168.1.1 --add --acl deny_103

python router_test.py -u HAUser -p 12345678 -r 192.168.1.1 --delete --acl deny_103

The script uses the telnetlib library to control the router.

To Do:

* Error Checking (Currently there is no error checking)
* Listing of ACLs
* Creation of ACLs
* Creation of Binding policies
* etc

This is the first version of this script, and is being used with our Home Automation to enforce network lockouts for the kids computers.  

usage: 

router_test.py [options]

Configure the Router.

optional arguments:

  -h, --help                          show this help message and exit
  
  -p PASSWORD, --password PASSWORD    Password to login with
  
  -r ROUTER, --router ROUTER          Routers IP address, e.g. 192.168.1.222
  
  -u USERNAME, --username USERNAME    Username to login with
  
  --acl ACL             acl to bind/unbind
  
  --add                 add the ACL
  
  --delete              remove the ACL
  

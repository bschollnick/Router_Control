Router_Control
==============

Control an TL-SG2008 Smart Switch via Telnet (for ACL Binding)

This is the first steps towards an Python script for controlling the SG2008, and similar switches from TP-Link.

This script will telnet into the router, and enable or disable an ACL Policy, as defined on the command line.

For example:

python router_test.py -u HAUser -p 12345678 -r 192.168.1.1 --add --acl deny_103

python router_test.py -u HAUser -p 12345678 -r 192.168.1.1 --delete --acl deny_103

The script uses the telnetlib library to control the router.

Current the script supports:

* Adding an pre-defined ACL to an active binding
* Removing an pre-defined ACL from the active bindings
* showing the ACL Bindings that are currently active


To Do:

* Error Checking (Currently there is no error checking)
* Creation of ACLs
* Creation of Binding policies

This is the first version of this script, and is being used with our Home Automation to enforce network lockouts for the kids computers.  

usage: 

router_test.py [options]

Configure the Router.

optional arguments:

  -h, --help                          show this help message and exit
  
  -p PASSWORD, --password PASSWORD    Password to login with
  
  -r ROUTER, --router ROUTER          Routers IP address, e.g. 192.168.1.222
  
  -u USERNAME, --username USERNAME    Username to login with
  
  --add [ACL1, ACL2, ...]                 add the ACL
  
  --delete [ACL1, ACL2, ...]             remove the ACL
  
  --show                                Show the ACL Binds that are in effect
  
  

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

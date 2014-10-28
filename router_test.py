import argparse
import sys
import telnetlib
import time

cr = "\r\n"

def parser_cmd ():

    parser=argparse.ArgumentParser(usage='\n\n%(prog)s [options]',
                                       description="\nConfigure the Router.\n\n",
                                       epilog="")
    parser.add_argument("-p", "--password", action="store", dest="password", help="Password to login with")
    parser.add_argument("-r", "--router", action="store", dest="router", help="Routers IP address, e.g. 192.168.1.222", required=True)
    parser.add_argument("-u", "--username", action="store", dest="username", help="Username to login with")
    parser.add_argument("-a", "--add", action="store", dest="add", nargs="*", help="add the ACL")
    parser.add_argument("-d", "--delete", action="store", dest="delete", nargs="*", help="remove the ACL")
    parser.add_argument("-s", "--show", action="store_true", dest="show", help="show the ACL binds that are in effect")

    args = parser.parse_args()
    return args

def switch_to_enabled_mode ( tnsession, hostname ):
    tnsession.write (cr)
    tnsession.write ("enable" + cr)
    tnsession.write (cr)
    test = tnsession.read_until ("%s#" % hostname, 1)

def return_hostname ( data_string ):
    hostname = data_string.split(cr)[1][:-1]
    print "hostname - %s" % hostname
    return hostname

def is_enabled_mode ( tnsession, hostname ):
    tnsession.write ( cr )
    test = tnsession.read_until ( hostname + "#", 1)
    x = test.split(cr)
    return x[-1]==hostname + "#"

def force_buffer_to_clear ( tn ):
    junk = tn.read_until ("ABCDEFGHIJ#", 1)     # FORCE THE telnet buffer to empty
    
def send_telnet ( flush_buffers = True, text_to_send = None, timeout = 1, tnsession = None):
    if tnsession == None:
        return
    
    if flush_buffers:
        force_buffer_to_clear ( tnsession )
        
    tn.write( command_to_send + cr)
    
def main ():
    args = parser_cmd ()
    HOST = args.router
    username = args.username
    password = args.password
#    acl = args.acl

    tn = telnetlib.Telnet(HOST)
    tn.read_until( "User:" )
    tn.write( username + cr)
    tn.read_until( "Password" )
    tn.write( password + cr)
    tn.write (cr)
    login_results = tn.read_until (">")
    hostname = return_hostname ( login_results )
    hostname_config = hostname+"(config)#"
    hostname_config_if = hostname+"(config-if)#"

    switch_to_enabled_mode ( tn, hostname )
    print "Logged in and Enabled Mode, ", is_enabled_mode (tn, hostname)
    tn.write (cr)
    tn.write ("configure" + cr)
    tn.write (cr)
    tn.write ("interface vlan 2" + cr)
    tn.write (cr)
    test = tn.read_until ("#")
    print "switch to interface mode results - "
    print "----------"
    for x in test.split(cr):
        print x
    print "----------"
    if args.add != [] and args.add != None:
        for acl in args.add:
            print "Adding bind for %s" % acl
            force_buffer_to_clear (tn)
            tn.write ("access-list bind %s" % acl + cr)
            test = tn.read_until (hostname_config_if,1)
            print "Adding Bind mode results - "
            if test.find("The policy-bind entry already exists.") != -1:
                print "\tBind already exists"
            elif test.find ("Policy is not defined.") != -1:
                print "\tPolicy has not been defined."
            elif len(test.split(cr)) > 2:
                print "\tPossible unknown error"
                print test.split(cr)
            print "----------"

    if args.delete != [] and args.delete != None:
        for acl in args.delete:
            print "removing bind for %s" % acl
            junk = tn.read_until ("ABCDEFGHIJ#", 1)     # FORCE THE telnet buffer to empty
            tn.write ("no access-list bind %s" % acl + cr)
            test = tn.read_until (hostname_config_if, 1)
            print "Removing Bind mode results - "
            if test.find("Policy-bind entry is not defined.") != -1:
                print "\tBind does not exist"
            elif len(test.split(cr)) > 2:
                print "\tPossible unknown error"
                print test.split(cr)
            print "----------"

    if args.show:
        junk = tn.read_until ("ABCDEFGHIJ#", 1)     # FORCE THE telnet buffer to empty
        tn.write ("show access-list bind" + cr)
        output = tn.read_until (hostname_config_if, 1)
        output = output.split (cr)
        data = []
        
        for x in output[4:]:
            print x                         # Output only at this point
            
            #
            #   Scrap the Data for later, when we add an API
            #
            temp = x.replace ("   ", " ")
            while temp.find ("  ") != -1:
                temp = temp.replace("  ", " ")
            temp = temp.split (" ") #   0 - index
                                    #   1 - policy name
                                    #   2 - interface / VID
                                    #   3 - Direction (e.g. Ingress or Egress)
                                    #   4 - Type (e.g. Vlan or Port)
            data.append ( temp[:-1] )
            # return data                                      
            
        
    tn.write ("exit" + cr)
    tn.write ("logout" + cr)

def split_output ( router_text ):
    output = []
    router_text = split ("\r\n")
#    for x in router_text:
#        if x.find ("\n") != -1:
            
if __name__ == "__main__":
    main()
# Route_Limit_Utilization_Factor
How to measure when a customer reaches route/prefix limit in Nokia boxes.

In some scenarios you might need to identify if any customer reaches the route/prefix limit. With this repo, it can be realized automatically, and everyone will be informed with suspected customer. 

TTP and Netmiko used to create this repo..

Sample config: 

===============================================================================
BGP Neighbor
===============================================================================
-------------------------------------------------------------------------------
Peer                 : 1.1.1.1
Description          : (Not Specified)
Group                : test
-------------------------------------------------------------------------------
Peer AS              : 0                Peer Port            : 0    
Peer Address         : 1.1.1.1
Local AS             : 15000            Local Port           : 0    
Local Address        : 0.0.0.0
Peer Type            : External         Dynamic Peer         : No
State                : Idle             Last State           : Idle
Last Event           : none
Last Error           : Unrecognized Error
Local Family         : IPv4
Remote Family        : (Not Specified)
Connect Retry        : 120              Local Pref.          : 100
Min Route Advt.      : 30               
Multihop             : 0 (Default)      AS Override          : Disabled
Damping              : Disabled         Loop Detect          : Ignore
MED Out              : No MED Out       Authentication       : None
Next Hop Self        : Disabled         AggregatorID Zero    : Disabled
Remove Private       : Disabled
Passive              : Disabled         
Peer Identifier      : 0.0.0.0          Fsm Est. Trans       : 0
Fsm Est. Time        : 13d02h12m        InUpd Elap. Time     : 13d02h12m
Hold Time            : 90               Keep Alive           : 30   
Min Hold Time        : 0                
Active Hold Time     : 0                Active Keep Alive    : 0    
Cluster Id           : None             Client Reflect       : Enabled
Preference           : 170              Num of Update Flaps  : 0    
Input Queue          : 0                Output Queue         : 0    
Input Messages       : 0                Output Messages      : 0    
Input Octets         : 0                Output Octets        : 0

snipped

MDT-Safi received    : 0                RT-Constrnt received : 0    
MDT-Safi active      : 0                RT-Constrnt active   : 0    
MDT-Safi suppressed  : 0                RT-Constrnt suppress*: 0    
MDT-Safi rejected    : 0                RT-Constrnt rejected : 0    
L2-VPN received      : 0                EVPN received        : 0    
L2-VPN active        : 0                EVPN active          : 0    
L2-VPN suppressed    : 0                EVPN suppressed      : 0    
L2-VPN rejected      : 0                EVPN rejected        : 0    
Flow-IPv4 received   : 0                Flow-IPv6 received   : 0    
Flow-IPv4 active     : 0                Flow-IPv6 active     : 0    
Flow-IPv4 suppressed : 0                Flow-IPv6 suppressed : 0    
Flow-IPv4 rejected   : 0                Flow-IPv6 rejected   : 0    
MS-PW received       : 0                BGP-LS received      : 0    
MS-PW active         : 0                BGP-LS active        : 0    
MS-PW suppressed     : 0                BGP-LS suppressed    : 0    
MS-PW rejected       : 0                BGP-LS rejected      : 0    
SRPLCY-IPV4 received : 0                SRPLCY-IPV6 received : 0    
SRPLCY-IPV4 active   : 0                SRPLCY-IPV6 active   : 0    
SRPLCY-IPV4 suppress*: 0                SRPLCY-IPV6 suppress*: 0    
SRPLCY-IPV4 rejected : 0                SRPLCY-IPV6 rejected : 0    

===============================================================================
Prefix Limits Per Address Family
===============================================================================
Family         Limit          Idle Timeout   Threshold Log Only  Post Import
-------------------------------------------------------------------------------
ipv4           1000000000     forever        90        Disabled  Disabled
evpn           10000000       forever        90        Disabled  Disabled
===============================================================================
* indicates that the corresponding row element may have been truncated.
-------------------------------------------------------------------------------
Neighbors shown : 1
===============================================================================
* indicates that the corresponding row element may have been truncated.


#vdi #idv #thinclient #thickclient #goldenImage

# VDI 
→ user can access remotely from their devices
→ connect through a broker, software based gateway

Store in SAN
Manage console the **GOLDEN IMAGE** (winver 21H2)
User data 

## server side VDI
hypervisor server host virtual disktop 
using golden image + user data on server

Server (computing device) –> thin client (basic networking for display)

## client side VDI
server send user data + golden image, run offline

Server → user data → thick client (get user data + golden image) 
- need good connection, syncing conflict

# IDV 
> Intelligent Desktop Virtualisation

Model for managing thin client and delivering virualised xomputing environment - IT can support and deployed

High performance PC (physically located same location as user)
→ virtualisation controlled at server for overall management 
→ but provide virtualised computing environment

Server –→ Computing Device –> end user  

# VDI vs IDV
| VDI                                                                        |                       | IDV                                                                                                                  |
| -------------------------------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Yes                                                                        | Remote Access         | No                                                                                                                   |
| expensive,  High performance Server for Virtualisation needed                     | cost saving           | No, high performance computing client needed , flexible, less server resource                                        |
| management in server, n lots of data need to transmit through the internet | security              | less datta is transfer internet (less exposure)                                                                      |
| control directly in server   external/server execution                     | centralised managment | faster access  (same place, better UX)   local execution                                                             |
| Best management // fully manage all user inside the server                 | management            | simply manage the virtualisation PC server at end point, less resource needed to complied at server-side             |
| it easily deploy imaging directly on server //no need external networking  | image deploying       | reduced complexity - deploy new image at distributed computing device                                                |
|                                                                            |                       | employs powerful computing resource through virtualisation layer, controlled through data center, run VM at end user |
| physically distant from user location                                      | location of VM        | at the same room of end user                                                                                         |
| fully rely on network, compute at server, transmit image , no offline      | network access        | Less rely on network and support offline system running                                                              |

# Diskless node
> why no comparsion betwrrn diskless node VS VDI or IDV?

iso/vhd/gho/img/ccd/sub/dmg

- store in centralised server
- no harddisk / thin client that only have ability to connect to internet
- one key recover/ not even saved

**Boot ROM by LAN from server signal**
PXE/ RPL/ iSCSi disk

### iPXE - smarter
→ use HTTP
→ iSCSI
→ with .kpxe file extension

## Protocol
DHCP → find server
TFTP → transfer required software ( basic method)
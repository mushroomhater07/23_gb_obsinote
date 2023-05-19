# Paper 2

- Database RDBMS
    - redundancy
    - inconsiitency
    - reduced data integrity
- JSON vs XML -
    
     standardise communication between server and client
    
    - understand
    - create
    - parse, native JavaScript + array
    - compact, expensive use?
    - data type
- SQL - Normalisation
    1. no repeating element / multiple in one record
    2. partial dependencies on compound key
    3. no dependencies on non key attribute
- Websocket
    - consist permant connection on TCP
    - real time
    - full duplex
    - no packet needed make use of space
- Client server
NAT port forwarding
DHCP
RoutablE ip > NAT
Ipv4 vs ipv6
- Structure of ip
    
    AND operation IP and Subnet Mask = Network ID
    
    AND operation IP and NOT(Subnet Mask) = Client ID
    
- Packet switching
    - Within LAN
        1. AND subnet mask
        2. compare
        3. same > find subnet ID
        4. not same send through router by packet
    - Packet switching
        1. sent independenty
        2. set sequence number
        3. hop forward until reach ( write different destination IP on Network ID
        4. depences on conjestion ( difference 
        5. hierchary order
- Csma/cs rts cts
    1. check channel clear or not
    2. send RTS if CTS recieved , data transmitted

Bit rate baud rate
Fetch decode execute

```
MAR ← [PC]
PC ← [PC ]+1
MBR ← Memory
CIR ← MBR
Decode
how execute work
Alu cu register bus
```

Von neumann harvard
Vernam cipher
Translator
OS
De morgan law

> Thick VS thin client
software installed
process power
> 

| Create | Retrieve | Update | Delete |
| --- | --- | --- | --- |
| write | retrieve | update | delete |
| POST | GET | PYT | DELETE |
| INSERT | SELECT | UPDATE | DELETE |

REST use HTTP request to interact with online DB

- Overflow
    
    result of a calculation
    is a number that is too large to store
    in the avaliable storage space / number of bits
    
- Vector bitmap
    
    Individual objects can be edited
    the image can be enlarged / scaled without loss of quality
    less file size(Large) images can be composed of relatively few objects 
    
- MIDI
    
    Music represented as sequence of MIDI (event) messages;
    •   Channel;
    •   Note on / note off;
    •   Pitch / frequency / note number;
    •   Volume / loudness;
    •   Velocity;
    •   Key pressure / aftertouch;
    •   Duration / length;
    •   Instrument;
    
    MIDI messages are usually two or three bytes long;
    MSB value of 1 indicates status byte, 0 indicates data bytes;
    Status bytes are divided into a command and a channel number (4 bits for each); Sixteen channels are supported;
    
- ADC
    - Analogue signal **A.** sound as BOD) sampled at fixed/regular time intervals
    - Amplitude/Voltage of signal/wave measured
    - Measurement coded into binary
- Floating VS Fixed?
    
    Floating: greater range ( more number
    
    Fixed: better for calculation
    
    Represents all numbers to a constant 
    
    fixed, precision/accuracy;
    
- Why rounding error?
    
    There are not enough bits in the mantissa,
    only 7 bits is not enough to represent 28.25 exactly // 
    It could be rounded to the nearest representable value // it may
    **R.** an error would be generated
    
- DHCP
    
    no need for expert to config host
    reduce time to config
    avoid duplicate IP
    
- non routable ip address
    
    which need a NAT to translate into a routable address before able to communicate => pass on to the internet
    

encryption =   (Using an algorithm) to convert a message into a form that is not understandable (without the key to decrypt it);
(Using an algorithm) to convert a message into a form that is only understandable by the intended parties // can only be read with the correct key;
(Using an algorithm) to convert a message into cipher text;

maritissa 1 . 000000    exponent 0111 (right)

Record locking - when a transaction start, it locked out until release
Timestamp - timestamp generated - result in loss of data integrity or incosistency cause if read and write

Digital signature Vs digital certificate

Certificate - a public key that publish by CA ensure you are real person

Baud rate, no of changes in one second

How data is transfer through a network stack??????\

ATNL stack

 Camera 

Lens light

Sensor adc pixel

 

Count 

Application 

Bespoke

Off the shelf

System

Utitly trans

1

Library
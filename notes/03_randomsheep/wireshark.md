# Wireshark

getpacket ubuntu- \
\`\`\` wiresharl\
`tcpdump`\
`ip addr`\
`tcpdump -l eth0 -w /tmp/http.pcap`\
` ``` `

`Open wireshark and look at pcap`

`Filter 7 ATNL`

` ``` wireshark `\
`http.host contains "baidu.com"`\
`http.request.method == "GET"`

`//look at the [Stream index: number]` \
`(apply as filter) || tcp.stream == 1`\
` ``` `

fin syn ack - handshake \
//view: flowgraph - limit to display filter

Follow> http stream\
&#x20;         \> tcp stream - HTTP website code\
search http\

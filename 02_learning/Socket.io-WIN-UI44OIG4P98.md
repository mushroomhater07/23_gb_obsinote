# socket.io-win-ui44oig4p98

!\[\[Pasted image 20230118112918.png]] !\[\[Pasted image 20230118112927.png]] !\[\[Pasted image 20230118112934.png]] !\[\[Pasted image 20230118112939.png]] _sdajs_

Fetch, ajax →hey server → client

`Websocket == 1 connection` (stayopen → server→client

\`Cors: firewall

server:              &#x20;

```Javascript
const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require ("socket.io")(server, {cors:{origin:["*"],},});
const port = 3000;

server.listen(port, ()=>{console.log("port" + port)}); 
//open server 3000
//socket.io begins
io.on("connection", (socket)=>{
    console.log(socket.id);
    socket.on("hello",(number,room)=>{
        io.emit("receive",number) //general emit
      socket.boardcast.emit //send to all not the client
      socket.to(room).emit( //send to room not client
      socket.broadcast.to(room).emit()
    })
   socket.on("hello",(room)=>{
socket.join(room)
   socket.on(“callback”,(message, cb)=>{
      cb(`Joined ${message}`
    })
```

client:

```Javascript
const socket = io();
    // console.log("hiis")
    socket.on("connect",()=>{
        console.log(`You have connected: ${socket.id}`)
    })
    $("#add").click(()=>{
        socket.emit("hello", "hello") 
        //send to all include itself
    })
    socket.on("receive", (message)=>{
        console.log("recieve: " + message)
    socket.emit("callback", (message)=>{ 
		//callback from emit
		 console.log(message)
    })
```

```Javascript
npm i @socket.io/admin-ui
const {instrument} = require('@socket.io/admin-ui')
instrument(io, {auth: false})
```

![](file:///C:/Users/Shalev/AppData/Local/Temp/msohtmlclip1/01/clip\_image005.png)

admin.socket.io ![](file:///C:/Users/Shalev/AppData/Local/Temp/msohtmlclip1/01/clip\_image006.png) Server URL": http://localhost:3000/admin Add \`cors:orgin: http://admin.socket.io

[https://www.youtube.com/watch?v=ZKEqqIO7n-k](https://www.youtube.com/watch?v=ZKEqqIO7n-k) please come back at 17:40 to finish watching it

!\[\[Pasted image 20230118113639.png]] !\[\[Pasted image 20230118113644.png]] !\[\[Pasted image 20230118113648.png]]

Object.values(objectvariable) →turn object into array JSON.stringtify(objectvar) → turn object into string wait for parse

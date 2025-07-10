const express = require ("express")
const app = express()

app.get('/',(req,res)=>{
    res.send("hello")
})

app.get('/raj',(req,res)=>{
    res.send("hello raj")
})
const port = 3000

app.listen(port,()=>{
    console.log(`server is running in port ${port}`);
    
})
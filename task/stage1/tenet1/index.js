const prop = require('dot-prop')
const tenet = require('./tenet.js')
const express = require('express')
const cookieParser = require('cookie-parser');
const fs = require('fs')
const app = express()
const port = 3000

function generateSecret(length){
    var result           = '';
    var characters       = 'xyz01';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

filePath = "./index.js"
cookieOpts = {maxAge: 90000, httpOnly: true, signed: true}
var secret = generateSecret(4);
console.log('secret', secret);
app.use(cookieParser(secret));
app.use(express.urlencoded({ extended: false }))

app.get('/', (req, res) => {
    // track visitors
    if(!req.signedCookies.visitor){
        var visitor = 'visitor_' + Math.random() * 16
        res.cookie('visitor', visitor, cookieOpts)
    }
    // make hzSession with cookies
    var hzSession = {
        'internal': {},
        'filePath': undefined
    }
    for(let item in req.signedCookies){
	console.log(item)
        prop.set(
            hzSession.internal,
            item,
            cookieParser.signedCookie(req.signedCookies[item])
        )
    }
    
    if(hzSession.filePath !== undefined){
        filePath = hzSession.filePath
    }

    fs.readFile(filePath, function (err, data){
        if(!err){
            res.send(tenet.reverse(data.toString()))
        } else {
            console.log(err)
        }
    })
})

app.listen(port, () => {
    console.log(`Listening on ${port}`)
})

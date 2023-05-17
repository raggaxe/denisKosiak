


const socketToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6IkNFMUE1NzE2MUQwNTlCQTlENDU3IiwicmVhZF9vbmx5Ijp0cnVlLCJwcmV2ZW50X21hc3RlciI6dHJ1ZSwidHdpdGNoX2lkIjoiNTgzNjQwNTQxIn0.0ayeWvvAlYE6mtytfNQAR5HiUg29HIqMfyqTshMf1qg'; //Socket token from /socket/token end point

//Connect to socket
const streamlabs = io(`https://sockets.streamlabs.com?token=${socketToken}`, {transports: ['websocket']});



streamlabs.on('event', (eventData) => {
    if (!eventData.for && eventData.type === 'donation') {
    //code to handle donation events
    console.log(eventData.message);
    }
    if (eventData.for === 'twitch_account') {
    console.log(eventData.type)

    switch(eventData.type) {
        case 'follow':
            //code to handle follow events
            console.log(eventData.message);
            var x = eventData.message;
        //     x.forEach(function(i){
        //     document.getElementById('name').innerHTML = '@'+ i.name;
        //     $("#anime").fadeIn(400);
        //     })
        //     setTimeout(function(){
        // $("#anime").fadeOut(400);
        // }, 10000)
            break;
        case 'subscription':
            //code to handle subscription events
            console.log(eventData.message);
            break;
        default:
            //default case
            console.log(eventData.message);
        }
    }
});
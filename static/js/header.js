function showElement(elementId) {
  var element = document.getElementById(elementId);
  element.style.display = 'block';
  element.style.animationName = 'slideUp';
}

function hideElement(elementId) {
  var element = document.getElementById(elementId);
  element.style.animationName = 'slideDown';
  setTimeout(function() {
      element.style.display = 'none';
  }, 500);
}

function toggleElements() {
  var linkElement = document.getElementById('link');
  var logoElement = document.getElementById('logo');

  if (linkElement.style.display === 'none') {
      showElement('link');
      hideElement('logo');
  } else {
      hideElement('link');
      showElement('logo');
  }
}

setInterval(toggleElements, 5000); // Alternar a visibilidade a cada 3 minutos (180000 milissegundos)



const socketToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6IjlFQjYyMDJEM0JEQTlFQTc5MzIyRDc0OTY3MTM2RkVGQkIxREQ0QTBGNDRCNjU5RTczODlBNjJFMzQ4RTc1NDdGNDNCMjM1NjhDNzhBN0FBRjIxNzU5QzQyMkEzRTk1QjgxRUVBMzhGQjgyRTA0NzRBMzk1RjhDMDgxQTBDN0JEQjY0OEIzRDM4NkRGMTBDRUM0MzAyMDYzNTdBN0Y3OUUxRjdCRjIzNDE0OTU2OTUwNTE2Q0Q4RjAzQzc3ODUwNDI3MTYxOTYwQzRFNkZBNkYxNzhDQ0RBMTIzNEJDQTJCQkJFNkQ3RjIyQjkwQjk5MDY1RDU1NzkzQkQiLCJyZWFkX29ubHkiOnRydWUsInByZXZlbnRfbWFzdGVyIjp0cnVlLCJ0d2l0Y2hfaWQiOiI0NzYwNzAzMjkifQ.9L768pd5i0t6Yb_n6tQoGS2k2LWl7yDyXpOZJ1-oS20'; //Socket token from /socket/token end point

const streamlabs = io(`https://sockets.streamlabs.com?token=${socketToken}`, { transports: ['websocket'] });

const follower = $('.follower');
const sub = $('.sub');
streamlabs.on('connect', () => {
  console.log('Conexão estabelecida com sucesso.');
});

streamlabs.on('event', (eventData) => {
  if (!eventData.for && eventData.type === 'donation') {
    //code to handle donation events
    console.log(eventData.message);
  }
  if (eventData.for === 'twitch_account') {
    console.log(eventData.type)

    switch (eventData.type) {
      case 'follow':
        //code to handle follow events
        console.log(eventData.message);
        var x = eventData.message;
        x.forEach(function (i) {
          follower.html('@' + i.name)
          $(".follow").fadeIn(400);
        })
        setTimeout(function () {
          $(".follow").fadeOut(400);
        }, 10000)

        break;
      case 'subscription':
        //code to handle subscription events  
        var p = eventData.message;
        console.log(p[0])
        p.forEach(function (i) {
          sub.html('@' + i.name)
          $(".subscribe").fadeIn(400);
          setTimeout(function() {
            var subScreen = document.querySelector(".sub-screen");
            subScreen.classList.add("expand");
          
            setTimeout(function() {
              subScreen.classList.remove("expand");
            }, 9000); // Tempo para aguardar antes de remover a classe "expand"
          
          }, 300); // Tempo para aguardar antes de adicionar a classe "expand"




        })
        setTimeout(function () {
          $(".subscribe").fadeOut(400);
        }, 10000)

        break;
      default:
        //default case
        console.log(eventData.message);
    }
  }
});
$(document).ready(function() {
  $(".follow").fadeOut(400);
  $(".subscribe").fadeOut(400);
});


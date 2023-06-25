var interval;
var totalSeconds = 0;

function startCountdown() {
    var timeInput = document.getElementById("timeInput");
    var countdown = document.getElementById("countdown");

    var time = timeInput.value;
    var timeArray = time.split(":");
    var hours = parseInt(timeArray[0]);
    var minutes = parseInt(timeArray[1]);
    var seconds = parseInt(timeArray[2]);

    if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
        return;
    }

    totalSeconds = hours * 3600 + minutes * 60 + seconds;
    if (totalSeconds <= 0) {
        return;
    }

    clearInterval(interval);

    interval = setInterval(function() {
        var formattedTime = formatTime(hours) + ":" + formatTime(minutes) + ":" + formatTime(seconds);

        countdown.innerHTML = formattedTime;

        if (totalSeconds <= 0) {
            clearInterval(interval);
            countdown.innerHTML = "Done!";
        }

        totalSeconds--;
        hours = Math.floor(totalSeconds / 3600);
        minutes = Math.floor((totalSeconds % 3600) / 60);
        seconds = totalSeconds % 60;
    }, 1000);
}

function pauseCountdown() {
    clearInterval(interval);
}

function formatTime(time) {
    return (time < 10) ? "0" + time : time;
}

$(document).ready(function() {
    $("#timeInput").inputmask("99:99:99", { placeholder: "00:00:00" });
    
        socket.emit('getTime');
});



 // 2. This code loads the IFrame Player API code asynchronously.
 var tag = document.createElement('script');

 tag.src = "https://www.youtube.com/AIzaSyBU6BL2zQjYzs_bA4hIms9j6uPoUJm8ATU";
 var firstScriptTag = document.getElementsByTagName('script')[0];
 firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

 // 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '2160',
    width: '3840',
    videoId: 's44apH1xY7k',
    playerVars: {
      autoplay: 1, // Habilitar autoplay
      controls: 0, // Remover controles do player
      showinfo: 0, // Remover informações do vídeo
      modestbranding: 1, // Remover logotipo do YouTube
      suggestedQuality: '2160p' // Definir qualidade de reprodução para 4K (2160p)
  
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}

// Restante do código permanece igual

 

 // 4. The API will call this function when the video player is ready.
 function onPlayerReady(event) {
   event.target.playVideo();
 }

 // 5. The API calls this function when the player's state changes.
 //    The function indicates that when playing a video (state=1),
 //    the player should play for six seconds and then stop.
 var done = false;
 function onPlayerStateChange(event) {
   if (event.data == YT.PlayerState.PLAYING && !done) {
     setTimeout(stopVideo, 6000);
     done = true;
   }
 }
 function stopVideo() {
   player.stopVideo();
 }
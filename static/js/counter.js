var interval;

function startCountdown() {
    var timeInput = document.getElementById("timeInput");
    var countdown = document.getElementById("countdown");

    var time = timeInput.value;
    var timeArray = time.split(":");
    var hours = parseInt(timeArray[0]);
    var minutes = parseInt(timeArray[1]);
    var seconds = parseInt(timeArray[2]);

    if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
        alert("Digite um valor válido para o tempo no formato HH:MM:SS.");
        return;
    }

    var totalSeconds = hours * 3600 + minutes * 60 + seconds;
    if (totalSeconds <= 0) {
        alert("Digite um valor válido para o tempo no formato HH:MM:SS.");
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

function formatTime(time) {
    return (time < 10) ? "0" + time : time;
}

$(document).ready(function() {
    $("#timeInput").inputmask("99:99:99", { placeholder: "00:00:00" });
});
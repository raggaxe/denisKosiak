
    let timerInterval;
    let currentTime = 0;
    let targetTime = 0;
    let isPaused = false;


    function startCountdown() {
    $('#start-button').hide()
    $('#pause-button').show()
     
      const inputTime = document.getElementById('countdown-display').textContent;
      const timeParts = inputTime.split(':');

      targetTime = (parseInt(timeParts[0]) * 3600) + (parseInt(timeParts[1]) * 60) + parseInt(timeParts[2]);
      currentTime = targetTime;
      isPaused = false;

      updateDisplay();

      clearInterval(timerInterval);
      const countdownDisplay = document.getElementById('countdown-display');
      socket.emit('setTimmer', {isPaused:isPaused, currentTime:countdownDisplay.textContent});
      
      timerInterval = setInterval(() => {
        if (!isPaused) {
          currentTime--;

          if (currentTime <= 0) {
            clearInterval(timerInterval);
            alert('Contagem regressiva concluída!');
          }

          updateDisplay();
        }
      }, 1000);
    }

    function pauseCountdown() {
      isPaused = !isPaused;
      const pauseButton = document.getElementById('pause-button');
      $('#start-button').hide()
      $('#pause-button').show()

      if (isPaused) {
        pauseButton.innerHTML = "<i class='bx bx-play-circle' ></i>";
      } else {
        pauseButton.innerHTML = "<i class='bx bx-pause-circle' ></i>";
      }

      const countdownDisplay = document.getElementById('countdown-display');
      socket.emit('setTimmer', {isPaused:isPaused, currentTime:countdownDisplay.textContent});
    }

    function resetCountdown() {
        $('#start-button').show()
        $('#pause-button').hide()
      clearInterval(timerInterval);
      currentTime = targetTime;
      isPaused = false;
      updateDisplay();
    }

    function updateDisplay() {
      const countdownDisplay = document.getElementById('countdown-display');
      const hours = Math.floor(currentTime / 3600);
      const minutes = Math.floor((currentTime % 3600) / 60);
      const seconds = currentTime % 60;
      countdownDisplay.textContent = `${formatTime(hours)}:${formatTime(minutes)}:${formatTime(seconds)}`;
    }

    function formatTime(time) {
      return time.toString().padStart(2, '0');
    }

    document.getElementById('start-button').addEventListener('click', startCountdown);
    document.getElementById('pause-button').addEventListener('click', pauseCountdown);
    document.getElementById('timmerCanvas').classList.add('active');

    function setTimmer(val, elem_val, elem, picker) {
      const countdownDisplay = document.getElementById('countdown-display');
      var selectedTime = val[1].toString(); // Tempo selecionado convertido para string no formato HH:MM:SS
      var targetTimeout = moment(selectedTime, "HH:mm:ss").valueOf(); // Tempo selecionado convertido em timestamp
      var timeNow = new Date().getTime(); // Tempo atual em timestamp
    
      var countdownTime = targetTimeout - timeNow; // Diferença de tempo em milissegundos
    
      // Verificar se a diferença de tempo é um valor válido
      if (countdownTime >= 0) {
        const countdownDuration = moment.duration(countdownTime); // Converter a diferença de tempo em uma duração Moment.js
    
        // Atualizar o tempo atual e o tempo alvo
        currentTime = countdownDuration.asSeconds();
        targetTime = targetTimeout;
        isPaused = false;
    
        // Formatar a duração em formato HH:MM:SS
        const formattedCountdown = moment.utc(countdownDuration.asMilliseconds()).format("HH:mm:ss");
        countdownDisplay.textContent = formattedCountdown;
    
        clearInterval(timerInterval);
        startCountdown();
      } else {
        countdownDisplay.textContent = "00:00:00";
        $('#start-button').hide()
        targetTime = 0;
        isPaused = false;
        clearInterval(timerInterval);
      }
      
      socket.emit('setTimmer', {isPaused:isPaused, currentTime:countdownDisplay.textContent});
 
    }




    socket.on('getTime status', function() {
      console.log('get')
      const countdownDisplay = document.getElementById('countdown-display');
      socket.emit('setTimmer', {isPaused:isPaused, currentTime:countdownDisplay.textContent});
    });
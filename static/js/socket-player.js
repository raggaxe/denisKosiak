var socket = io.connect('http:' + '//' + document.domain + ':' + location.port);

// socket.emit('getPlayers');



socket.on('getPlayer_1', function () {
  console.log('aceito')
});



const player1_name = $('#player1_name')
socket.on('setPlayer1_screen', function (data) {
  player1_name.html(data.name);
});


const player2_name = $('#player2_name')
socket.on('setPlayer2_screen', function (data) {
  player2_name.html(data.name);
});


const player3_name = $('#player3_name')
socket.on('setPlayer3_screen', function (data) {
  player3_name.html(data.name);
});


const player4_name = $('#player4_name')
socket.on('setPlayer4_screen', function (data) {
  player4_name.html(data.name);
});


const input_score1 = $('#input_score1')
const input_score2 = $('#input_score2')
const input_score3 = $('#input_score3')
const input_score4 = $('#input_score4')

socket.on('score1', function (data) {
  if (data.score < parseInt(input_score1.val())) {
    scoreMenos(data.score, '#player1_score')
  }
  if (data.score > parseInt(input_score1.val())) {
    scoreMais(data.score, '#player1_score')
  }

  input_score1.val(data.score);
});
socket.on('score2', function (data) {
  if (data.score < parseInt(input_score2.val())) {
    scoreMenos(data.score, '#player2_score')
  }
  if (data.score > parseInt(input_score2.val())) {
    scoreMais(data.score, '#player2_score')
  }

  input_score2.val(data.score);
});

socket.on('score3', function (data) {
  console.log('atual', data.score)
  console.log('antigo', parseInt(input_score3.val()))
  if (data.score < parseInt(input_score3.val())) {
    scoreMenos(data.score, '#player3_score')
  }
  if (data.score > parseInt(input_score3.val())) {
    scoreMais(data.score, '#player3_score')
  }

  input_score3.val(data.score);
});
socket.on('score4', function (data) {
  if (data.score < parseInt(input_score4.val())) {
    scoreMenos(data.score, '#player4_score')
  }
  if (data.score > parseInt(input_score4.val())) {
    scoreMais(data.score, '#player4_score')
  }


  input_score4.val(data.score);
})



function score(_score, insertDiv) {
  getTemplate().then(function (template) {
    // Adiciona a nova div usando o template
    for (let i = 0; i < parseInt(_score); i++) {
      $(insertDiv).append(template);
    };
  });
}
function scoreMais(_score, insertDiv) {
  getTemplate().then(function (template) {
    // Adiciona a nova div usando o template
    $(insertDiv).append(template);
  });
}

function scoreMenos(_score, insertDiv) {
  // Remove a última div adicionada
  const scoreDivs = $(insertDiv + ' .score-container');

  if (scoreDivs.length > parseInt(_score)) {

    $(scoreDivs[scoreDivs.length - 1]).remove();
  }
}



function getTemplate() {
  return new Promise(function (resolve, reject) {
    $.ajax({
      url: '/score_template',
      type: 'GET',
      success: function (data) {
        resolve(data);
      },
      error: function (xhr, status, error) {
        reject(error);
      }
    });
  });
}


$(document).ready(function () {

  score(input_score1.val(), '#player1_score')
  score(input_score2.val(), '#player2_score')
  score(input_score3.val(), '#player3_score')
  score(input_score4.val(), '#player4_score')
});







socket.on('set-spinName', function (data) {
 $('#'+data.position).attr('data-result', data.name);
 $('#name_'+data.position).html(data.name);
})



socket.on('spin', function () {
  spinWheel();
});


socket.on('refresh stream', function () {
  if (window.location.pathname === '/stream') {
    location.reload();
  }
});

socket.on('countDown', function (data) {
  console.log(data)
  $('#timeInput').val(data['currentTime'])
  $("#countdown").html(data['currentTime']);

  if (!data['isPaused']){
    startCountdown()
  }
  else{
    pauseCountdown()
  }
  
});

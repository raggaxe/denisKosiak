var socket = io.connect('http:' + '//' + document.domain + ':' + location.port);




  const player1_name = $('#player1_name');
  const player2_name = $('#player2_name');
  const player3_name = $('#player3_name');
  const player4_name = $('#player4_name');


  player1_name.on('keyup', function() {
    socket.emit('set_player1', {name: $(this).val() }); //
  });
  player2_name.on('keyup', function() {
    socket.emit('set_player2', {name: $(this).val() }); //
  });

  player3_name.on('keyup', function() {
    socket.emit('set_player3', {name: $(this).val() }); //
  });
  player4_name.on('keyup', function() {
    socket.emit('set_player4', {name: $(this).val() }); //
  });


const player1_score = $('#player1_score');
const player2_score = $('#player2_score');
const player3_score = $('#player3_score');
const player4_score = $('#player4_score');

player1_score.on('input', function() {
  socket.emit('set_score1', {score: $(this).val() }); //
});
player2_score.on('input', function() {
  socket.emit('set_score2', {score: $(this).val() }); //
});
player3_score.on('input', function() {
  socket.emit('set_score3', {score: $(this).val() }); //
});
player4_score.on('input', function() {
  socket.emit('set_score4', {score: $(this).val() }); //
});

//   socket.on('player2_name_resp', function() {
//     console.log('player2_name_resp')
//   });




const spinName = $('.spin-name');
const spinNow = $('.spin-now');
spinName.on('input', function() {
  socket.emit('spinName', { name: $(this).val(), position: $(this).attr('data-position') });
});

spinNow.on('click', function() {
  socket.emit('spinNow');
});


$(document).ready(function() {
  socket.emit('refresh');
});




socket.on('connect', function() {
  socket.emit('connected', { message: 'User connected' });
});



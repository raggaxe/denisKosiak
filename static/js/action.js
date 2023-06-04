
const input_player = $('#input_player') 
const input_game = $('#input_game')
const cards_player = $('.card')


$( document ).ready(function() {
    if (input_player.val() != '') { 
        var optionPlayer = $('#select_player option[value="' + input_player.val() + '"]')
        optionPlayer.prop('selected', true);
        cards_player.each(function(index, element) {
            if (index+1 <= parseInt(input_player.val()) ){
                $(element).show();
            }
           
        });

    }
    if (input_game.val() != ''){
        var optionGame = $('#select_game option[value="' + input_game.val() + '"]')
        optionGame.prop('selected', true);
    }

    socket.emit('update');


});


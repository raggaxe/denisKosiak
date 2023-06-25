from flask import session, request, send_from_directory, current_app, Blueprint, jsonify, redirect, \
    render_template, url_for, flash
from repository.BaseRepository import BaseRepository
from Configs.MongoConfig import MongoConfig


mod = Blueprint('player_routes', __name__)
repository = BaseRepository(MongoConfig().get_connect())




def getFilename():
    configs = repository.find_one('configs', {'creator': 'Denis Kosiak'})
    filename = ''
    if configs is not None:
        if configs['game'] == 'Sport':
            filename = 'Sport.png'

        if configs['game'] == 'Race':
            filename = 'Race.png'

        if configs['game'] == 'FPS':
            filename = 'FPS.png'
            
        if configs['game']== 'Logo':
            filename = 'FlagLogo.png'

        return filename

@mod.route('/player1')
def player1():
    try:

        return render_template('placarView/player1.html' , player = repository.find_one('players', {'position':'1'}) )
    except  Exception as e:
        print(e)

        
@mod.route('/player2')
def player2():
    return render_template('placarView/player2.html', player = repository.find_one('players', {'position':'2'}), )
@mod.route('/player3')
def player3():
    return render_template('placarView/player3.html' , player = repository.find_one('players', {'position':'3'}))
@mod.route('/player4')
def player4():
    return render_template('placarView/player4.html', player = repository.find_one('players', {'position':'4'}))


@mod.route('/score_template')
def score_template():
    configs = repository.find_one('configs', {'status': True})
    return render_template('shared/score.html', configs=configs, filename=getFilename())
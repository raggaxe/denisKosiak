from flask import Flask, render_template,request
from flask_socketio import *
from dotenv import load_dotenv
import os
from model.Player import Player
from Configs.MongoConfig import MongoConfig
from repository.BaseRepository import BaseRepository
from bson import json_util, ObjectId


repository = BaseRepository(MongoConfig().get_connect())

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")
app.config['SERVER_NAME'] = '0.0.0.0'
socketio = SocketIO(app, async_handlers=True)


@app.route('/placarView')
def placarView():
   
   
    return render_template('placarView/index.html',
                            player1 = repository.find_one('players', {'position':'1'}) , 
                            player2 = repository.find_one('players', {'position':'2'}), 
                            player3 = repository.find_one('players', {'position':'3'}) , 
                            player4 = repository.find_one('players', {'position':'4'}) ,
                              )
    
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('set_player1')
def set_player1(data):
    print(data)
    player_found = repository.find_one('players', {'position':'1'})
    if player_found is not None:
        print('atualizar player')
        print(player_found['_id'])
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'name':data['name'] })
        print('atualizado')
        print(atual)
        
    else:
        form = {
            'name':data['name'],
            'position':'1',
            'score': '0'
        }
        new_player = Player(form)
        repository.create(new_player)
    emit('setPlayer1_screen',{'name':data['name']},broadcast=True)
 





@socketio.on('set_player2')
def set_player2(data):
    print(data)
    player_found = repository.find_one('players', {'position':'2'})
    if player_found is not None:
        print('atualizar player')
        print(player_found['_id'])
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'name':data['name'] })
        print('atualizado')
        print(atual)
        
    else:
        form = {
            'name':data['name'],
            'position':'2',
            'score': '0'
        }
        new_player = Player(form)
        repository.create(new_player)
    emit('setPlayer2_screen',{'name':data['name']},broadcast=True)



@socketio.on('set_player3')
def set_player3(data):
    print(data)
    player_found = repository.find_one('players', {'position':'3'})
    if player_found is not None:
        print('atualizar player')
        print(player_found['_id'])
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'name':data['name'] })
        print('atualizado')
        print(atual)
        
    else:
        form = {
            'name':data['name'],
            'position':'3',
            'score': '0'
        }
        new_player = Player(form)
        repository.create(new_player)
    emit('setPlayer3_screen',{'name':data['name']},broadcast=True)


@socketio.on('set_player4')
def set_player4(data):
    print(data)
    player_found = repository.find_one('players', {'position':'4'})
    if player_found is not None:
        print('atualizar player')
        print(player_found['_id'])
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'name':data['name'] })
        print('atualizado')
        print(atual)
        
    else:
        form = {
            'name':data['name'],
            'position':'4',
            'score': '0'
        }
        new_player = Player(form)
        repository.create(new_player)
    emit('setPlayer4_screen',{'name':data['name']},broadcast=True)

@socketio.on('set_score1')
def set_score1(data):
    print(data)
    player_found = repository.find_one('players', {'position':'1'})
    if player_found is not None:
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'score':data['score'] })
        emit('score1',{'score': int(atual['score'])},broadcast=True)
        
    else:
        form = {
            'name':'',
            'position':'1',
            'score': 0
        }
        new_player = Player(form)
        repository.create(new_player)
        emit('score1',{'score':0},broadcast=True)
    
 




@socketio.on('set_score2')
def set_score2(data):
    print(data)
    player_found = repository.find_one('players', {'position':'2'})
    if player_found is not None:
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'score':data['score'] })
        emit('score2',{'score':int(atual['score'])},broadcast=True)
        
    else:
        form = {
            'name':'',
            'position':'2',
            'score': data['score']
        }
        new_player = Player(form)
        repository.create(new_player)
        emit('score2',{'score':0},broadcast=True)


@socketio.on('set_score3')
def set_score3(data):
    print(data)
    player_found = repository.find_one('players', {'position':'3'})
    
    if player_found is not None:
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'score':data['score'] })
        emit('score3',{'score':int(atual['score'])},broadcast=True)
        
    else:
        form = {
            'name':'',
            'position':'3',
            'score': data['score']
        }
        new_player = Player(form)
        repository.create(new_player)
        emit('score3',{'score':0},broadcast=True)




@socketio.on('set_score4')
def set_score4(data):
    print(data)
    player_found = repository.find_one('players', {'position':'4'})
    if player_found is not None:
        atual = repository.update_one('players', {'_id': ObjectId(player_found['_id'] ) }, {'score':data['score'] })
        emit('score4',{'score':int(atual['score'])},broadcast=True)
    else:
        form = {
            'name':'',
            'position':'4',
            'score': data['score']
        }
        new_player = Player(form)
        repository.create(new_player)
    emit('score4',{'score':0},broadcast=True)




@app.route('/player1')
def player1():
    try:
        return render_template('placarView/player1.html' , player = repository.find_one('players', {'position':'1'}) )
    except  Exception as e:
        print(e)
@app.route('/player2')
def player2():
    return render_template('placarView/player2.html', player = repository.find_one('players', {'position':'2'}))
@app.route('/player3')
def player3():
    return render_template('placarView/player3.html' , player = repository.find_one('players', {'position':'3'}) )
@app.route('/player4')
def player4():
    return render_template('placarView/player4.html', player = repository.find_one('players', {'position':'4'}))


@app.route('/score_template')
def score_template():
    return render_template('shared/score.html')



@app.route('/denis',methods=['GET', 'POST'])
def josh():
    return render_template('twitch.html')

if __name__ == '__main__':
    socketio.run(app,debug=True)
 
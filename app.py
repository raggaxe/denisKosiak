from flask import Flask, render_template,request,send_from_directory, current_app, redirect, url_for
from flask_socketio import *
from dotenv import load_dotenv
import os
from model.Spin import Spin
from model.Player import Player
from Configs.MongoConfig import MongoConfig
from repository.BaseRepository import BaseRepository
from bson import json_util, ObjectId

from controllers import AdminRoutes,  PlayersRoutes


repository = BaseRepository(MongoConfig().get_connect())

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")
# app.config['SERVER_NAME'] = '0.0.0.0'
socketio = SocketIO(app, async_handlers=True)

blueprints = [
    AdminRoutes.mod,
    PlayersRoutes.mod,
]

for bp in blueprints:
    app.register_blueprint(bp)

    
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('update')
def update():
    print('Client update')


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



@socketio.on('spinName')
def spinName(data):
    print(data)
    name_found = repository.find_one('spin', {'position':data['position']})
    
    if name_found is not None:
        repository.update_one('spin', {'_id': ObjectId(name_found['_id'] ) }, {'name':data['name'] })
        print('updated name')
    else:
        form = {
            'name':data['name'],
            'position':data['position'],
        }
        new_spin_name= Spin(form)
        repository.create(new_spin_name)

    emit('set-spinName',{'name':data['name'],'position':data['position']},broadcast=True)


@socketio.on('spinNow')
def spinName():
    print('spinNow')
    emit('spin',broadcast=True)

@socketio.on('refresh')
def refresh():
    emit('refresh stream',broadcast=True)

@socketio.on('setTimmer')
def setTimmer(data):
    emit('countDown',data,broadcast=True)

@socketio.on('getTime')
def getTime():
 
    emit('getTime status',broadcast=True)

@app.route('/')
def home():
    return 'HELLO'


if __name__ == '__main__':
    socketio.run(app,debug=True)
    # app.run()
 
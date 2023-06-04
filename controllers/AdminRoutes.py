from flask import session, request, send_from_directory, current_app, Blueprint, jsonify, redirect, \
    render_template, url_for, flash
from repository.BaseRepository import BaseRepository
from Configs.MongoConfig import MongoConfig
from werkzeug.utils import secure_filename
from model.Config import InitConfig
mod = Blueprint('admin_routes', __name__)
repository = BaseRepository(MongoConfig().get_connect())


############### fotos uploads ##################
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@mod.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)





############### Dashboard ##################
@mod.route('/denisKosiak')
def placarView():
    configs = repository.find_one('configs', {'creator':'Denis Kosiak'})
    filename = ''
    if configs is not None:
        if configs['game']== 'Sport':
            filename = 'Sport.png'

        if configs['game']== 'Race':
            filename = 'Race.png'

        if configs['game']== 'FPS':
            filename = 'FPS.png'


    return render_template('placarView/index.html',
                            configs=configs, 
                            filename=filename,
                            player1 = repository.find_one('players', {'position':'1'}) , 
                            player2 = repository.find_one('players', {'position':'2'}), 
                            player3 = repository.find_one('players', {'position':'3'}) , 
                            player4 = repository.find_one('players', {'position':'4'}) ,
                              )



@mod.route('/configs',methods=['GET', 'POST'])
def configs():
    if request.method == 'POST':
        print(request.form)
        configs = repository.find_one('configs', {'creator':'Denis Kosiak'})
        if configs is not None:
            repository.update_one('configs',{'creator':'Denis Kosiak'},{'players':request.form['players'],'game':request.form['game']})
        else:
            new_configs = InitConfig(request.form)
            repository.create(new_configs)
        return redirect(url_for('admin_routes.placarView'))




@mod.route('/stream-denis',methods=['GET','POST'])
def stream():
    configs = repository.find_one('configs', {'creator':'Denis Kosiak'})
    stream = []
    if configs is not None:
        createStream = int(configs['players'])
        for i in range(createStream):
            print(f"Iteration {i+1}")
            stream.append({
                'player': i+1,
                'template':render_template(f'placarView/player{i+1}.html' , player = repository.find_one('players', {'position':f'{i+1}'}) )
            })       
    return render_template('stream/index.html',stream=stream) 





# @mod.route('/setImage', methods=['POST', 'GET'])
# def setImage():
#     file = request.files.get('file')
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
#     return redirect(url_for('placarView'))
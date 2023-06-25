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
        
        if configs['game']== 'Logo':
            filename = 'FlagLogo.png'

    spin_name_1 = repository.find('spin', {'position': '1'})
    spin_name_2 = repository.find('spin', {'position': '2'})
    spin_name_3 = repository.find('spin', {'position': '3'})
    spin_name_4 = repository.find('spin', {'position': '4'})
    spin_name_5 = repository.find('spin', {'position': '5'})
    spin_name_6 = repository.find('spin', {'position': '6'})
    spin_name_7 = repository.find('spin', {'position': '7'})
    spin_name_8 = repository.find('spin', {'position': '8'})

    # Verifica se os resultados existem e converte-os em listas
    spin_name_1_list = list(spin_name_1) if spin_name_1 else []
    spin_name_2_list = list(spin_name_2) if spin_name_2 else []
    spin_name_3_list = list(spin_name_3) if spin_name_3 else []
    spin_name_4_list = list(spin_name_4) if spin_name_4 else []
    spin_name_5_list = list(spin_name_5) if spin_name_5 else []
    spin_name_6_list = list(spin_name_6) if spin_name_6 else []
    spin_name_7_list = list(spin_name_7) if spin_name_7 else []
    spin_name_8_list = list(spin_name_8) if spin_name_8 else []

    return render_template('placarView/index.html',
                            configs=configs, 
                            filename=filename,
                            player1 = repository.find_one('players', {'position':'1'}) , 
                            player2 = repository.find_one('players', {'position':'2'}), 
                            player3 = repository.find_one('players', {'position':'3'}) , 
                            player4 = repository.find_one('players', {'position':'4'}) ,
                            spin_name_1=spin_name_1_list,
                            spin_name_2=spin_name_2_list,
                            spin_name_3=spin_name_3_list,
                            spin_name_4=spin_name_4_list,
                            spin_name_5=spin_name_5_list,
                            spin_name_6=spin_name_6_list,
                            spin_name_7=spin_name_7_list,
                            spin_name_8=spin_name_8_list
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




@mod.route('/stream',methods=['GET','POST'])
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


@mod.route('/denis-stream',methods=['GET','POST'])
def denis_stream():

    return render_template('stream/denis-stream.html',names_spin=names_spin) 


@mod.route('/header',methods=['GET','POST'])
def header():
    return render_template('stream/header.html') 

@mod.route('/frame',methods=['GET','POST'])
def frame():
    return render_template('stream/frame.html') 

@mod.route('/counter',methods=['GET','POST'])
def counter():
    return render_template('stream/counter.html') 

@mod.route('/spinning',methods=['GET','POST'])
def spinning():
    spin_name_1 = repository.find('spin', {'position': '1'})
    spin_name_2 = repository.find('spin', {'position': '2'})
    spin_name_3 = repository.find('spin', {'position': '3'})
    spin_name_4 = repository.find('spin', {'position': '4'})
    spin_name_5 = repository.find('spin', {'position': '5'})
    spin_name_6 = repository.find('spin', {'position': '6'})
    spin_name_7 = repository.find('spin', {'position': '7'})
    spin_name_8 = repository.find('spin', {'position': '8'})

    # Verifica se os resultados existem e converte-os em listas
    spin_name_1_list = list(spin_name_1) if spin_name_1 else []
    spin_name_2_list = list(spin_name_2) if spin_name_2 else []
    spin_name_3_list = list(spin_name_3) if spin_name_3 else []
    spin_name_4_list = list(spin_name_4) if spin_name_4 else []
    spin_name_5_list = list(spin_name_5) if spin_name_5 else []
    spin_name_6_list = list(spin_name_6) if spin_name_6 else []
    spin_name_7_list = list(spin_name_7) if spin_name_7 else []
    spin_name_8_list = list(spin_name_8) if spin_name_8 else []
    return render_template('stream/spinning.html',
                            spin_name_1=spin_name_1_list,
                            spin_name_2=spin_name_2_list,
                            spin_name_3=spin_name_3_list,
                            spin_name_4=spin_name_4_list,
                            spin_name_5=spin_name_5_list,
                            spin_name_6=spin_name_6_list,
                            spin_name_7=spin_name_7_list,
                            spin_name_8=spin_name_8_list
                            ) 

# @mod.route('/setImage', methods=['POST', 'GET'])
# def setImage():
#     file = request.files.get('file')
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
#     return redirect(url_for('placarView'))
class InitConfig(object):
    def __init__(self, form):
        self.collection_name = 'configs'
        self.creator = 'Denis Kosiak'
        self.players =form['players']
        self.game=form['game']
        self.status = True
       

    
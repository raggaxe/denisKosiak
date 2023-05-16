class Player(object):
    def __init__(self, form):
        self.collection_name = 'players'
        self.position = form['position']
        self.name = form['name']
        self.score = form['score']

    
{"filter":false,"title":"models.py","tooltip":"/flaskblog/models.py","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":0,"column":0},"end":{"row":19,"column":60},"action":"insert","lines":["class User(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(20), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')","    password = db.Column(db.String(60), nullable=False)","    posts = db.relationship('Post', backref='author', lazy=True)","","    def __repr__(self):","        return f\"User('{self.username}', '{self.email}', '{self.image_file}')\"","","class Post(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    title = db.Column(db.String(100), nullable=False)","    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)","    content = db.Column(db.Text, nullable=False)","    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)","","    def __repr__(self):","        return f\"Post('{self.title}', '{self.date_posted}')\""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":4},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":5},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["f"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["l"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["a"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["s"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["k"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"remove","lines":[" "],"id":7},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"remove","lines":["k"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"remove","lines":["s"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"remove","lines":["a"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"remove","lines":["l"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["f"]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["r"],"id":8},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["u"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":[" "],"id":9},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["i"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["m"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["p"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["o"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["r"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":[" "],"id":10},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["d"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["b"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":29},"action":"insert","lines":["from datetime import datetime"],"id":12}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["n"],"id":13},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["u"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["r"]}],[{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["_"],"id":14},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["_"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["a"],"id":15},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["i"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["n"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["_"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":0,"column":0},"end":{"row":23,"column":60},"action":"remove","lines":["from datetime import datetime","from __main__ import db","","","class User(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(20), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')","    password = db.Column(db.String(60), nullable=False)","    posts = db.relationship('Post', backref='author', lazy=True)","","    def __repr__(self):","        return f\"User('{self.username}', '{self.email}', '{self.image_file}')\"","","class Post(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    title = db.Column(db.String(100), nullable=False)","    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)","    content = db.Column(db.Text, nullable=False)","    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)","","    def __repr__(self):","        return f\"Post('{self.title}', '{self.date_posted}')\""],"id":16}],[{"start":{"row":0,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["from datetime import datetime","from flaskblog import db","","","class User(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(20), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')","    password = db.Column(db.String(60), nullable=False)","    posts = db.relationship('Post', backref='author', lazy=True)","","    def __repr__(self):","        return f\"User('{self.username}', '{self.email}', '{self.image_file}')\"","","","class Post(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    title = db.Column(db.String(100), nullable=False)","    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)","    content = db.Column(db.Text, nullable=False)","    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)","","    def __repr__(self):","        return f\"Post('{self.title}', '{self.date_posted}')\"",""],"id":17}],[{"start":{"row":0,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["from datetime import datetime","from flaskblog import db","","","class User(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(20), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')","    password = db.Column(db.String(60), nullable=False)","    posts = db.relationship('Post', backref='author', lazy=True)","","    def __repr__(self):","        return f\"User('{self.username}', '{self.email}', '{self.image_file}')\"","","","class Post(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    title = db.Column(db.String(100), nullable=False)","    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)","    content = db.Column(db.Text, nullable=False)","    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)","","    def __repr__(self):","        return f\"Post('{self.title}', '{self.date_posted}')\"",""],"id":18},{"start":{"row":0,"column":0},"end":{"row":24,"column":60},"action":"insert","lines":["from datetime import datetime","from flaskblog import db","","","class User(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(20), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')","    password = db.Column(db.String(60), nullable=False)","    posts = db.relationship('Post', backref='author', lazy=True)","","    def __repr__(self):","        return f\"User('{self.username}', '{self.email}', '{self.image_file}')\"","","","class Post(db.Model):","    id = db.Column(db.Integer, primary_key=True)","    title = db.Column(db.String(100), nullable=False)","    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)","    content = db.Column(db.Text, nullable=False)","    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)","","    def __repr__(self):","        return f\"Post('{self.title}', '{self.date_posted}')\""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":24,"column":60},"end":{"row":24,"column":60},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":30,"mode":"ace/mode/python"}},"timestamp":1566611921280,"hash":"d12728e0b0e9a656b403550849290a90edf1304d"}
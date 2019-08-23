{"changed":true,"filter":false,"title":"microblog.py","tooltip":"/microblog.py","value":"from flask import Flask, render_template, request\n\n# adding in functionality to access the operating system\nimport os\n\napp = Flask(__name__)\n\n@app.route('/hello')\ndef foobar():\n    return render_template(\"hello.html\")\n\n@app.route('/greet_the_person', methods=['POST'])\ndef process_form():\n    print(request.form)\n    n = request.form.get('person_name')\n    age = request.form.get('age')\n    return \"Hi, {}, welcome to the website!\".format(n)\n\n\n# @app.route('/hello', methods=['GET', 'POST'])\n# def foobar():\n#     if request.method == 'GET':\n#         return render_template(\"hello.html\")\n#     elif request.method == 'POST':\n#         print(request.form)\n#         n = request.form.get('person_name')\n#         age = request.form.get('age')\n#         return \"Hi, {}, welcome to the website\".format(n)\n\n# \"magic code\" -- boilerplate\nif __name__ == '__main__':\n    app.run(host=os.environ.get('IP'),\n            port=int(os.environ.get('PORT')),\n            debug=True) ","undoManager":{"mark":-2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":19},"action":"insert","lines":["from app import app"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":19},"action":"remove","lines":["from app import app"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":33,"column":24},"action":"insert","lines":["from flask import Flask, render_template, request","","# adding in functionality to access the operating system","import os","","app = Flask(__name__)","","@app.route('/hello')","def foobar():","    return render_template(\"hello.html\")","","@app.route('/greet_the_person', methods=['POST'])","def process_form():","    print(request.form)","    n = request.form.get('person_name')","    age = request.form.get('age')","    return \"Hi, {}, welcome to the website!\".format(n)","","","# @app.route('/hello', methods=['GET', 'POST'])","# def foobar():","#     if request.method == 'GET':","#         return render_template(\"hello.html\")","#     elif request.method == 'POST':","#         print(request.form)","#         n = request.form.get('person_name')","#         age = request.form.get('age')","#         return \"Hi, {}, welcome to the website\".format(n)","","# \"magic code\" -- boilerplate","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True) "],"id":3}]]},"ace":{"folds":[],"scrolltop":56,"scrollleft":0,"selection":{"start":{"row":33,"column":24},"end":{"row":33,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1566594551632}
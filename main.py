<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def rewrite_index():
    from app import server
    serverName = server.getServerName()

    return render_template('index.tpl', server=serverName)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)
=======
#!/usr/bin/env python
__author__ = 'David Poslt'


>>>>>>> 2f874f82a7a51707149ea4f613353fd0e7ef529c

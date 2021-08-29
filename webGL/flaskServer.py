#独自Flaskサーバを使用するとき　→　Aproach.pyと連携をとる
from flask import Flask, request
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')
 
@app.route('/StreamingAssets/PHP', methods=['POST'])
def updateScore():
    print('post');
    
    filename = 'StreamingAssets/PHP/' + request.form['filename']
    score = request.form['score']
    print(filename);
    print(score);
    with open(filename, 'w') as fout:
        fout.write(score)
    print('writed!');
        
    return score

app.run(host='127.0.0.1', port=8005, debug=True)

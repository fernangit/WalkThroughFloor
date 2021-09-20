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
    option = request.form['option']
    score = request.form['score']
    comment = request.form['comment']
    print(filename);
    print(score);
    print(comment);
    text = score + comment
    with open(filename, option) as fout:
        fout.write(text)
    print('writed!');
        
    return score

app.run(host='127.0.0.1', port=8005, debug=True)

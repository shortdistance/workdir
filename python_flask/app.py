from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def helloworld():
    return 'hello world!'


@app.route('/', methods=['GET'])
def rob():
    return render_template('1.html')

@app.route('/api/user/change_staus', methods=['POST'])
def change_user_status():
    email = request.json['email']
    status = int(request.json['status'])
    print email, status
    return jsonify(info='success')

if __name__ == "__main__":
    app.run('0.0.0.0', 1000, debug=True)

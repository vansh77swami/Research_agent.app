from flask import Flask, render_template, request, redirect, url_for
import requests
import mistune 

app = Flask(__name__)
app.secret_key = 'somesecretkey'

@app.route('/getResponse', methods=['GET'])
def get_response():
    query = request.args.get('query', default = '*', type = str)
    headers = {
        'x-api-key': '330fuseless'
    }
    response = requests.post(
        "https://research-agent-v1ur.onrender.com/",
        headers=headers,
        json={"query": query}
    )
    if response.status_code == 200:
        response_text = mistune.markdown(response.json())
    else:
        response_text = 'Error occurred while fetching the result.'

    return response_text


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/paper')
def paper():
    return app.send_static_file('subdir/paper.html')

if __name__ == '__main__':
    app.run(debug=True)
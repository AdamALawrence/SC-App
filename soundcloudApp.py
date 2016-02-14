from flask import Flask, render_template
import soundcloud
import requests

app = Flask(__name__)

@app.route('/')
def index():
	

	r = requests.get('https://api.soundcloud.com/users/3207?client_id=7746f4238b8d4a91259513decb853667')



	return render_template('index.html', a = "hi guys", request = r)







if __name__ == '__main__':
	app.run(debug=True)
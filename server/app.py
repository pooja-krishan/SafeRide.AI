from flask import Flask

import utils.speechToText, utils.sentimentAnalysis, utils.speechToText
app = Flask(__name__)

@app.route('/')
def intro():
    return utils.speechToText.getStreamStatus()

if __name__ == "__main__":
    app.run(debug=True)

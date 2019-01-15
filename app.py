from flask import Flask
import plotly.plotly as py
import plotly.graph_objs as go
app = Flask(__name__)

@app.route("/")
def plot():
	data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    	)]
	py.iplot(data, filename='basic-bar')
    
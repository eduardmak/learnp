from flask import Flask, request
import getweather as gw

app = Flask(__name__)

# print(gw.get_weather())


@app.route("/")
def index():
	return "HI!"




@app.route("/name")
def news():
	g = [request.args.get(item) for item in request.args]
	return "Год: %s" %  g


# @app.route("/names/<int:name>")
# def names(name):
# 	for item in request.args:
# 		print(item)
# 		print(request.args.get(item))
# 	return "Новость: %s" % name

if __name__ == '__main__':
	app.run()
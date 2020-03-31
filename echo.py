import flask
# loading Flask library and creating a Flask object
app = flask.Flask(__name__)

# define a predict function as an endpoint  with a Flask annotation that specifies that the function should be hosted 
# at '/' and accesible by HTTP Get and Post.
@app.route("/", methods=["GET","POST"])
def predict():
    # define sucess key as False
    data = {"success": False}
    
    # check for passed in parameters (did the caller passed in arguments?)
    params = flask.request.json
    if params is None:
        params = flask.request.args
    
    # if parameters are found, echo the msg parameter 
    if "msg" in params.keys(): 
        data["response"] = params.get("msg")
        data["success"] = True
        
    # return a response in json format 
    return flask.jsonify(data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
import functions_framework as functions
 
 functions.http('helloHttp', (req, res) => {


    request_json = req.get_json(silent=True)
    request_args = req.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    res.send('Hello {}!'.format(name));

   );}

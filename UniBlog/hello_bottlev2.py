import bottle

@bottle.route('/')
def home_page():
    return "hello markus\n"

@bottle.route('/testpage')
def test_page():
    return "this is a test page\n"

bottle.debug(True)
bottle.run(host="localhost", port=8080)

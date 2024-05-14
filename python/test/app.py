def application(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html'),('Header1', "lalala"),('Header2', "hahaha")])
    return [b'<h1>Hello web!</h1>']

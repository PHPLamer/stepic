def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    body = env.get('QUERY_STRING').replace('&', '\r\n')
    return [body]

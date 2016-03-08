def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = env.get('QUERY_STRING').replace('&', '<br>')
    return [body]

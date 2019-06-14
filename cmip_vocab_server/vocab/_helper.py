def get_server_url(request):
    """
    Get the server URL from the request object.

    @param request

    @return a str containing the server URL
    """
    server = '{}://{}'.format(request.scheme, request.get_host())
    return server

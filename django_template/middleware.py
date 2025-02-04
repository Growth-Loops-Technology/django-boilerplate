class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            # Strip 'Bearer ' prefix if it exists
            token = auth_header[7:]
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
        
        response = self.get_response(request)
        return response
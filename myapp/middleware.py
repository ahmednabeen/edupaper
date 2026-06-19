from django.utils.deprecation import MiddlewareMixin


class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data: https://images.unsplash.com https://plus.unsplash.com; "
            "frame-src 'self'; "
            "frame-ancestors 'self'; "
            "require-trusted-types-for 'script'"
        )
        response['Cross-Origin-Opener-Policy'] = 'same-origin'
        response['X-Content-Type-Options'] = 'nosniff'
        return response

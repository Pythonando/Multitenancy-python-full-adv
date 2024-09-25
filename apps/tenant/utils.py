def get_current_request():
    from .middleware import RequestMiddleware
    return RequestMiddleware.request_local.current_request
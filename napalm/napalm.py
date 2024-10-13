from webob import Request, Response
from parse import parse
import inspect
from requests import Session as RequestsSession
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from typing import Callable, Any

class Napalm(object):
    """
    Init the properties of a Napalm instance
    """
    def __init__(self):
        self.routes: dict[str, Callable[[Request, Response, Any], Any]] = {}
        
    """
    Start the Napalm application with some initial state. It loads the request and changes the response accordingly to it
    """
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self._handle_request(request)

        return response(environ, start_response)
            
    """
    PRIVATE METHOD
    Returns a default response in case of route not found.
    """
    def _default_response(self, response: Response):
        response.status_code = 404
        response.text = "Not Found"

    """
    PRIVATE METHOD
    Tries to find the handler associated with the route typed within the url.
    """
    def _find_handler(self, request_path: str):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
            
        return None, None
            
    """
    PRIVATE METHOD
    Handle the current request on your application.
    """
    def _handle_request(self, request: Request):
        response: Response = Response()

        handler, kwargs = self._find_handler(request_path=request.path)
            
        if handler is not None:
            if inspect.isclass(handler):
                handler_function = getattr(handler(), request.method.lower(), None)
                if handler_function is None:
                    raise AttributeError("Method Not Allowed!", request.method)
                handler_function(request, response, **kwargs)
            else:
                handler(request, response, **kwargs)
        else:
            self._default_response(response)
        
        return response
    
    def _add_route(self, path: str, handler: Callable[[Request, Response, Any], Any]):
        assert path not in self.routes, "Such route already exists."

        self.routes[path] = handler
    
    def route(self, path: str) -> Callable[[Request, Response, Any], Any]:
        def wrapper(handler: Callable[[Request, Response, Any], Any]) -> Callable[[Request, Response, Any], Any]:
            self._add_route(path, handler)
            return handler

        return wrapper

    def test_session(self, base_url="http://testserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))

        return session
    
    def run(self):
        pass
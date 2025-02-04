from typing import Optional, Callable, Dict
from models import Response


class API:
    def __init__(self):
        self.routes: Dict[tuple[str, str], Callable] = {}
    
    def route(self, path: str, methods: str, query_params: Optional[dict] = None):
        def wrapper(self, func: Callable) -> Callable:
            for method in methods:
                self.routes[(path, method)] = func
            return func
        return wrapper
    
    def handle_request(self, path: str, method: str, query_params: Optional[dict] = None) -> Response:
        route = self.routes.get({path, method})
        if route:
            return route(query_params)
        else:
            return Response(status=404, message="Not Found")

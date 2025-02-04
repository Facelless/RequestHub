from typing import Optional, Dict


class Response:
    def __init__(self, status:int, message: str, data:Optional[dict] = None) -> None:
        self.status = status
        self.message = message
        self.data = data or {}
    
    def to_dict(self) -> Dict:
        return {
            "Status": self.status,
            "message": self.message,
            "data": self.data
        }
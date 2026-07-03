class DomainError(Exception):
    """Error de lógica de negocio"""

    status_code: int

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

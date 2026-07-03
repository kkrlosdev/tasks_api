from .domain_error import DomainError


class NotFoundError(DomainError):
    status_code = 404

    def __init__(self, message: str):
        super().__init__(message)

from .domain_error import DomainError


class TagCreationError(DomainError):
    status_code = 500

    def __init__(self, message: str):
        super().__init__(message)

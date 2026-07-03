from .domain_error import DomainError


class TagAlreadyExistsError(DomainError):
    status_code = 409

    def __init__(self, message: str):
        super().__init__(message)

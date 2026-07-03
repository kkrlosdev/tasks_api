from .domain_error import DomainError


class InvalidTaskStatusError(DomainError):
    status_code = 400

    def __init__(self, message: str):
        super().__init__(message)

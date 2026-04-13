class NotFoundError(Exception):
    pass

class DomainError(Exception):
    """Error de lógica de negocio"""
    pass

class CriticityAlreadyExistsError(DomainError):
    pass

class CriticityCreationError(DomainError):
    pass

class TagAlreadyExistsError(DomainError):
    pass

class TagCreationError(DomainError):
    pass
from typing import Union


class CustomException(Exception):
    DEFAULT_ERROR_MESSAGE = "Exception occurred"

    def __init__(
        self,
        error_message: Union[str, None] = None,
        error_code: Union[str, None] = None,
        field: Union[str, None] = None,
    ):
        error_message = error_message or self.DEFAULT_ERROR_MESSAGE
        self.error_message = error_message
        self.error_code = error_code
        self.field = field
        super().__init__(self.error_message)


class RecordNotFoundException(Exception):
    def __init__(self, message="Record not found"):
        self.message = message
        super().__init__(self.message)


class ObjectNotFoundException(Exception):
    def __init__(self, message="Record not found", status_code=404):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ValueErrorException(ValueError):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ApiException(CustomException):
    DEFAULT_ERROR_MESSAGE = "API Exception"
    error_code = "AE901"

class BaseResponse:
    def __init__(self):
        self.status = False
        self.summary = None
        self.error = {}
        self.data = None

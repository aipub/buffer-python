class BufferException(Exception):
    def __init__(self, raw_response):
        self.code = 0
        if isinstance(raw_response, dict):
            self.code = raw_response.get('code',0)
            message = raw_response.get('error', 'Unknown Exception')
        else:
            message = raw_response

        # Call the base class constructor with the parameters it needs
        super(BufferException, self).__init__(message)

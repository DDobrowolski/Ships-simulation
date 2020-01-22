class Container:
    def __init__(self, source_port, destination_port, content_type):
        self._source_port = source_port
        self._destination_port = destination_port
        self._content_type = content_type

    @property
    def destination_port(self):
        return self._destination_port

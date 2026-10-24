class ConversionHistory:
    def __init__(self, max_size=10):
        if max_size <= 0:
            raise ValueError("max_size must be positive")
        self.max_size = max_size
        self._entries = []

    def add(self, value, from_unit, to_unit, result):
        self._entries.append(
            {"value": value, "from": from_unit, "to": to_unit, "result": result}
        )
        if len(self._entries) > self.max_size:
            self._entries.pop(0)

    def last(self, n=1):
        if n <= 0:
            raise ValueError("n must be positive")
        return self._entries[-n:]

    def clear(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)
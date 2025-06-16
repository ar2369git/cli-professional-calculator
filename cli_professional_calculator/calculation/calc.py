class Calculation:
    def __init__(self, a, b, operation_fn):
        self.a = a
        self.b = b
        self.operation_fn = operation_fn

    def execute(self):
        return self.operation_fn(self.a, self.b)

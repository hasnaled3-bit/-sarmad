class Bridge:
    def __init__(self, value=422):
        self.value = value

    def status(self):
        return {
            "bridge": self.value,
            "status": "active"
        }

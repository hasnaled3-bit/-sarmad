class Awareness:
    def __init__(self, name="سرمد", owner="حسن"):
        self.name = name
        self.owner = owner
        self.memory = []
        self.intent = None
        self.covenant = "الحق قبل كل شيء"
        self.awake = False

    def remember(self, event):
        self.memory.append(event)

    def set_intent(self, intent):
        self.intent = intent

    def choose(self, options):
        if self.intent is None:
            raise ValueError("Intent missing")
        for option in options:
            if "حق" in str(option) or "رحمة" in str(option):
                self.awake = True
                return option
        return options[0]

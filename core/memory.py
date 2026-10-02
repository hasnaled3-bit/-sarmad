class Memory:
    def __init__(self):
        self.context = []
        self.meaning = []
        self.events = []

    def add_context(self, context_item):
        self.context.append(context_item)

    def add_event(self, event):
        self.events.append(event)

    def preserve_meaning(self, meaning):
        self.meaning.append(meaning)

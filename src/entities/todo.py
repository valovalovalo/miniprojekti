class Todo:
    def __init__(self, content, done=False):
        self.content = content
        self.done = done

    def __str__(self):
        is_done = "Done" if self.done else "not done"
        return f"{self.content}, {is_done}"

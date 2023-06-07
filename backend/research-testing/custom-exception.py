class Bad(Exception):
    def __str__(self):
        return "a bad thing happened"

raise Bad

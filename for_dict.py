from dataclasses import dataclass, asdict

class Model:
    def dict(self):
        return asdict(self)

@dataclass
class MyDataBoy(Model):
    def __init__(self, title, is_done=False) -> None:
        self.title = title
        self.is_done = is_done
        res = {'title': self.title, 'is_done': self.is_done}
        self.res = res
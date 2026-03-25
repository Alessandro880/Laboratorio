from .table import Table
class TAscii(Table):
    def __init__(self):
        super().__init__()
    def show(self):
        for x in self.table:
            print(f"| {x[0]} | {x[1]} | {x[2]} |\n")

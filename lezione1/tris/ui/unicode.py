from .table import Table
class TUnicode(Table):
    def __init__(self):
        super().__init__()
    def show(self):
        for i,x in enumerate(self.table):
            print(f" {x[0]} │ {x[1]} │ {x[2]} ")
            if i < 2:
                print("───┼───┼───")

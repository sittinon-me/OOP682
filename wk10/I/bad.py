class Machine:
    def print(self,document):
        pass
    def scan(self,document):
        pass
    def fax(self,document):
        pass

class OldPrint(Machine):
    def print(self, document):
        print("printing")
    def scan(self,document):
        raise NotImplementedError("print mai dai")
    def fax(self,document):
        raise NotImplementedError("fax mai dai")
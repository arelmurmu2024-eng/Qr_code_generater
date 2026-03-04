class Qcode:
    def __init__(self, data :str = "Noting") -> None:
        """Takes data (string) and converts it into qrcode and saves it as image"""
        import qrcode as qc

        self.qr_code_name :str = self.gen_qrname()

        self.data :str = data
        qr_code = qc.make(data)
        qr_code.save(self.qr_code_name) # type: ignore
    
    def gen_qrname(self) -> str:
        """Generates random qrcode names"""
        import random,string

        name = f"Cache/{random.choice([x for x in (string.ascii_lowercase)])}{random.randint(1, 100)}.png"

        return name
    
    def return_name(self) -> str:
        """Returnes the generated qr code name including usable path"""

        return self.qr_code_name


name = Qcode()

class tell_vokaler():

    def __init__(self, tekst):
       vokal = "AEIOÆØÅU"
       x = sum(tekst.count(vokaler) for vokaler in vokal)
       print(x)

class speilvend():
    def __init__(self, tekst):
        tekst = tekst[::-1]
        print(tekst)

class erstatt_vokaler():

    def __init__(self, tekst):
        self.vokal = "AEIOÆØÅUaeioæøå"
        self.tekst = tekst


    def erstatt_vokalerfunksjon(self, ny_vokal):
        for vokal in self.vokal:
           self.tekst = self.tekst.replace(vokal, ny_vokal)
        print(self.tekst)
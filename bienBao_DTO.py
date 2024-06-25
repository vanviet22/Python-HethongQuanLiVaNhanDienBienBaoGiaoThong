class bienbao():
    def __init__(self, ten,ynghia, img):
        self._tenBien = ten
        self._imgPath = img
        self._yNghia=ynghia

    def get_tenBien(self):
        return self._tenBien
    def get_yNghia(self):
        return self._yNghia
    def set_yNghia(self,ynghia):
        self._yNghia=ynghia
    def set_tenBien(self, ten):
        self._tenBien = ten

    def get_imgPath(self):
        return self._imgPath

    def set_imgPath(self, img):
        self._imgPath = img

    tenBien = property(get_tenBien, set_tenBien)
    imgPath = property(get_imgPath, set_imgPath)
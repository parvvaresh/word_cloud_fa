import json


class Fonts:
    def __init__(self) -> None:
        
        with open("./fonts/info.json", "r") as file:
            self.info_fonts = json.load(file)
        
    def SetFont(self, name : str) -> str:
        if name not in self.info_fonts:
            raise ValueError(f"The font '{name}' does not exist.")
        else:
            return self.info_fonts[name]
    
    def getInfo(self) -> list:
        return list(self.info_fonts.keys())
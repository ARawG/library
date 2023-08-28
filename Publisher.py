class Publisher:
    def __init__(self, id:int, name:str, location:str) -> None:
        self.id = id
        self.name = name
        self.location = location

    def get_info(self) -> str:
        return (f"Id of publisher:{str(id)} \n publisher name:{self.name}\n publisher location:{self.location}")
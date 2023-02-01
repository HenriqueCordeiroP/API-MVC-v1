class Livros:
    def __init__(self, id : int, title : str, author :str):
        self.id = id
        self.title = title
        self.author = author

    def return_json(self):
        return f'{{"author":"{self.author}", "id":{self.id}, "title":"{self.title} "}} '
    

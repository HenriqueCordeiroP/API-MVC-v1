from flask import jsonify
class ApiEndpoints:
    book_list = []
    def read(self):
        if len(self.book_list) < 1:
            return "No books here."
        else:
            return jsonify(self.book_list)
    
    def create(self, book):
        if book in self.book_list:
            return "duplicate item"
        else:
            self.book_list.append(book)
        return jsonify(self.book_list)

    def update_method(self, id : int, updated_book):
        for index, book in enumerate(self.book_list):
            if book['id'] == id:
                self.book_list[index].update(updated_book)
                break
        return jsonify(self.book_list)

    def delete(self, id : int):
        for index, book in enumerate(self.book_list):
            if book['id'] == id:
                del self.book_list[index]
                break
        return jsonify(self.book_list)
    

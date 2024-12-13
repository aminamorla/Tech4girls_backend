from flask import Flask, jsonify,request
from config import session
from backend_crud import Backend_Crud
from books import books_bp

app = Flask(__name__)
app.register_blueprint(books_bp)
backend_crud = Backend_Crud(session)


@app.route("/")
def home():
    return "Welcome To Flask"


books = [
    {"id":1, "title": "1984", "author": "George Orwell"},
    {"id":2, "title": "To Kill  A Mockingbird", "author": "Harper Lee"},
    {"id":3, "title": "You", "author": "Caroline Kepnes"}
]
@app.route("/books", methods=['GET'])
def get_all_books():
    return jsonify(books), 200

@app.route("/books/<int:book_id>", methods=['GET'])
def get_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book), 200
        
        return jsonify({"error": "Book not found"}), 404
    
@app.route("/books/<string:author>", methods=['GET'])
def get_book_by_author(author):
    for book in books:
        if book["author"] == author:
            return jsonify(book), 200
        
@app.route("/books", methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({"new book added": new_book})

@app.route("/books/<int:book_id>", methods=['PATCH'])
def add_book_by_id(book_id):
    updation_data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update(updation_data)
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:book_id>", methods=['DELETE'])
def delete_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            book.remove(book)
            return jsonify({"message": f'Book with ID {book_id} has been deleted'})
        return jsonify({"error": "Book not found"}), 404




@app.route('/students', methods= ['GET'])
def get_all_students():
    students = backend_crud.get_all_students() 
    students_list = []
    for student in students:
        students_list.append({
            "id": student.student_id,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "email": student.email
            })
    return jsonify(students_list)

@app.route('/student/<strings:first_name>', methods=['GET'])
def get_by_first(first_name):
    student = backend_crud.get_all_students_by_first(first_name)
    return jsonify({
            "id": student.student_id,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "email": student.email
            })


"""@app.route('/students', methods=['POST'])
def add_student():
    details = request.get_json()
    new_student = backend_crud.insert_student(
        first_name = details.get('first_name'),
        last_name = details.get('last_name'),
        email = details.get('email'),
        age = details.get('age')
    )
    return jsonify({"new student added": {
    "id": new_student.student_id
    "first_name": new_student.first_name
    "last_name": new_student.last_name
    "email": new_student.email
    
    }})"""
    

if __name__ == '__main__':
    app.run(debug=True)
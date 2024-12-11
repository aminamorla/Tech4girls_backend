from config import Session
from models import MyLaptops
from flask import session

class Laptop_crud:
    def _init_(self):
        self.session = Session
        
    def insert_laptop(self, student_id, laptop_name, laptop_number):
        new_laptop = MyLaptops( student_id=student_id, laptop_name=laptop_name, laptop_number=laptop_number)
        self.session.add(new_laptop)
        self.session.commit()
        return f"Student with ID: {student_id} has a laptop named '{laptop_name}' with number: {laptop_number}"
    
    def get_all_laptops(self):
        return self.session.query(MyLaptops).all()
    
    def get_laptop_by_name(self, laptop_name):
        return session.query(MyLaptops).filter_by(laptop_name=laptop_name).first()
    
    def update_laptop(self, student_id, laptop_number = None, laptop_name= None):
        selected_laptop = self.session.query(MyLaptops).filter_by(student_id=student_id).first()
        if selected_laptop:
            if laptop_number:
                selected_laptop.laptop_number = laptop_number
            if laptop_name:
                selected_laptop.laptop_name = laptop_name
            session.commit()
        return selected_laptop   
    
    def delete_laptop(self,student_id):
        laptop_del = self.session.query(MyLaptops).filter_by(student_id=student_id).first()
        if laptop_del:
            session.delete(laptop_del)
        session.commit()
        return f'Student with id:{student_id} has been removed'
        


laptop_crud = Laptop_crud()

""" Add a student"""
# add_laptop = laptop_crud.insert_laptop(2,'Hp', 2010)
# print(add_laptop)

"""Get all laptop from the database"""
# get_laptop = laptop_crud.get_all_laptops()
# for laptop in get_laptop:
#     print(laptop)

"""Get laptop by name"""
# get_laptop_name = laptop_crud.get_laptop_by_name('Jennifer')
# print(get_laptop_name)

"""Update Laptop"""
# update_lap = laptop_crud.update_laptop(1, laptop_name='Light')
# print(update_lap)

"""Delete a laptop"""
# del_lap = laptop_crud.delete_laptop(4)
# print(del_lap)
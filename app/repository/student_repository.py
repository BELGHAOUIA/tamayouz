from supabase import Client
from app.repository.supabase_repository import Supabase


class StudentRepository:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def save_student(self, student_data):
        return Supabase.insert_data("student",student_data,self.supabase)
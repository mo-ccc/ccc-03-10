import unittest
from main import create_app, db
import json

class TestBooks(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()
        
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])
    
    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def test_book_index(self):
        response = self.client.get("/books/")
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
    
    def test_delete(self):
        response = self.client.get("/books/")
        data = response.get_json()
        initial_length = len(data)
        
        response = self.client.delete(f"/books/{initial_length}")
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get("/books/")
        data = response.get_json()
        final_length = len(data)
        
        self.assertEqual(initial_length-1, final_length)
        
    def test_post(self):
        body = {"title":"harry potter"}
        x = self.client.post("/books/", json=body, follow_redirects=False)
        self.assertEqual(x.status_code, 200)
        
        response = self.client.get("/books/")
        data = response.get_json()
        self.assertEqual(data[len(data)-1], {"id": len(data), "title":"harry potter"})
        
    
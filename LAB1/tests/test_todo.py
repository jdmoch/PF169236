import unittest
from src.todo import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()

    def add_task(self):
        todo = TodoList()
        todo.add_task("Kup mleko")
        self.assertIn("Kup mleko", todo.get_active_tasks())

    def complete_task(self):
        todo = TodoList()
        todo.add_task("Zrobić ćwiczenia")
        todo.complete_task("Zrobić ćwiczenia")
        self.assertIn("Zrobić ćwiczenia", todo.get_completed_tasks())
        self.assertNotIn("Zrobić ćwiczenia", todo.get_active_tasks())

    def complete_nonexistent_task(self):
        todo = TodoList()
        with self.assertRaises(ValueError):
            todo.complete_task("Nieistniejące zadanie")

    def get_active_tasks(self):
        todo = TodoList()
        todo.add_task("Czytać książkę")
        todo.add_task("Zrobić pranie")
        self.assertEqual(todo.get_active_tasks(), ["Czytać książkę", "Zrobić pranie"])

    def get_completed_tasks(self):
        todo = TodoList()
        todo.add_task("Zjeść obiad")
        todo.complete_task("Zjeść obiad")
        self.assertEqual(todo.get_completed_tasks(), ["Zjeść obiad"])

    def test_add_empty_task(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.complete_task("Task 1")
        self.todo_list.complete_task("Non-existent task")

        self.assertNotIn("Non-existent task", self.todo_list.get_completed_tasks())
        self.assertNotIn("Non-existent task", self.todo_list.get_active_tasks())

if __name__ == "__main__":
    unittest.main()

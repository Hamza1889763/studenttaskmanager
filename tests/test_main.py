
import unittest
from unittest.mock import patch
import main


class TestStudentTaskManager(unittest.TestCase):

    def setUp(self):
        main.tasks.clear()

    @patch("builtins.input", return_value="Complete Assignment")
    def test_add_task(self, mock_input):
        main.add_task()

        self.assertEqual(len(main.tasks), 1)
        self.assertEqual(main.tasks[0]["title"], "Complete Assignment")
        self.assertFalse(main.tasks[0]["completed"])

    @patch("builtins.input", return_value="1")
    def test_complete_task(self, mock_input):
        main.tasks.append({
            "id": 1,
            "title": "Study Python",
            "completed": False
        })

        main.complete_task()

        self.assertTrue(main.tasks[0]["completed"])

    @patch("builtins.input", return_value="1")
    def test_delete_task(self, mock_input):
        main.tasks.append({
            "id": 1,
            "title": "Submit Assignment",
            "completed": False
        })

        main.delete_task()

        self.assertEqual(len(main.tasks), 0)


if __name__ == "__main__":
    unittest.main()

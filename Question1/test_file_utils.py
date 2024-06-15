import unittest
import os

def get_contents(fname: str):
    try:
        with open(fname, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
    except IOError:
        return None

class TestGetContents(unittest.TestCase):

    def setUp(self):
        self.test_file_name = "test_file.txt"
        with open(self.test_file_name, 'w') as file:
            file.write("file content")

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_file_exists(self):
        result = get_contents(self.test_file_name)
        self.assertEqual(result, "file content")

    def test_file_not_found(self):
        result = get_contents("nonexistent_file.txt")
        self.assertIsNone(result)

    def test_empty_file(self):
        empty_file_name = "empty_file.txt"
        with open(empty_file_name, 'w') as file:
            pass  
        try:
            result = get_contents(empty_file_name)
            self.assertEqual(result, "")
        finally:
            os.remove(empty_file_name)

if __name__ == "__main__":
    unittest.main()
import unittest
import os

def get_contents(fname: str):
    try:
        with open(fname, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
    except IsADirectoryError:
        return None

class TestGetContents(unittest.TestCase):

    def setUp(self):
        self.test_file_name = "test_file.txt"
        with open(self.test_file_name, 'w') as file:
            file.write("file content")

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_file_exists(self):
        result = get_contents(self.test_file_name)
        self.assertEqual(result, "file content")

    def test_file_not_found(self):
        result = get_contents("nonexistent_file.txt")
        self.assertIsNone(result)

    def test_empty_file(self):
        empty_file_name = "empty_file.txt"
        with open(empty_file_name, 'w') as file:
            pass  
        try:
            result = get_contents(empty_file_name)
            self.assertEqual(result, "")
        finally:
            os.remove(empty_file_name)

    def test_directory_error(self):
        directory_name = "test_directory"
        os.mkdir(directory_name)
        try:
            result = get_contents(directory_name)
            self.assertIsNone(result)
        finally:
            os.rmdir(directory_name)

if __name__ == "__main__":
    unittest.main()

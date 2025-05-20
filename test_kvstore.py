import unittest
from kvstore import KeyValueStore

class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.kv = KeyValueStore()

    def test_create_and_read(self):
        self.assertEqual(self.kv.create("key1", "value1")[0], True)
        self.assertEqual(self.kv.read("key1")[1], "value1")

    def test_create_existing_key(self):
        self.kv.create("key1", "value1")
        self.assertEqual(self.kv.create("key1", "value2")[0], False)

    def test_update(self):
        self.kv.create("key1", "value1")
        self.assertEqual(self.kv.update("key1", "new")[0], True)
        self.assertEqual(self.kv.read("key1")[1], "new")

    def test_delete(self):
        self.kv.create("key1", "value1")
        self.assertEqual(self.kv.delete("key1")[0], True)
        self.assertEqual(self.kv.read("key1")[0], False)

if __name__ == "__main__":
    unittest.main()

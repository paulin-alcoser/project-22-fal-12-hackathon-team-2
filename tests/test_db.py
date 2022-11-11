import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict

from app import TimelinePost 

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!') #0
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!') #1
        assert second_post.id == 2

        posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at)]
        assert len(posts) == 2
        assert 1 == 2
        # Testing to see if names are equal
        self.assertEqual(posts[0]["name"], 'John Doe', "The names are not the same.")
        self.assertEqual(posts[1]["name"], 'Jane Doe', "The names are not the same")
        # Testing to see if emails address are equal
        self.assertEqual(posts[0]["email"], 'john@example.com', "The names are not the same.")
        self.assertEqual(posts[1]["email"], 'jane@example.com', "The names are not the same")
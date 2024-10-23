import unittest
from sqlalchemy import create_engine, Column, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models.database import Base, Session
from models.dish_state import Category
from ui.mainwindow import new_turn_number


class TestNewTurnNumber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_new_turn_number_first_entry(self):
        result = new_turn_number()
        self.assertEqual(result, 1, "Перший виклик повинен повернути 1, якщо таблиця порожня")

    def test_new_turn_number_with_existing_data(self):
        category = Category(turn_number=5)
        self.session.add(category)
        self.session.commit()

        result = new_turn_number()
        self.assertEqual(result, 6, "Повинно повернути 6, оскільки найбільший turn_number був 5")

    def test_new_turn_number_with_zero_turn_number(self):
        category = Category(turn_number=0)
        self.session.add(category)
        self.session.commit()

        result = new_turn_number()
        self.assertEqual(result, 1, "Якщо найбільший turn_number = 0, наступний повинен бути 1")

    def test_new_turn_number_with_multiple_records(self):
        categories = [Category(turn_number=1), Category(turn_number=3), Category(turn_number=10)]
        self.session.add_all(categories)
        self.session.commit()
        result = new_turn_number()
        self.assertEqual(result, 11, "Повинно повернути 11, оскільки найбільший turn_number був 10")



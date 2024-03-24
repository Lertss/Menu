from models.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Session


class Case(Base):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    name_eng = Column(String)
    description = Column(String)
    description_english = Column(String)
    price = Column(Integer)
    masa = Column(Integer)
    case_state = Column(Integer, ForeignKey('case_state.id'))
    category = Column(Integer, ForeignKey('category.id'))

    def __init__(self, name: str = "", name_eng: str = "", description: str = "",
                 description_english: str = "", price: str = "", masa: str = "", category: str = ""):
        self.name = name
        self.name_eng = name_eng
        self.description = description
        self.description_english = description_english
        self.price = price
        self.masa = masa
        self.category = category
        self.case_state = 2

    def update_state(self):
        session = Session()
        session.query(Case).filter(Case.id == self.id).update({Case.case_state: self.case_state})
        session.commit()
        session.close()

    @staticmethod
    def delete_case(case_id):
        session = Session()
        case_to_delete = session.query(Case).filter_by(id=case_id).first()
        if case_to_delete:
            session.delete(case_to_delete)
            session.commit()
            session.close()
            print(f'Справа с ID {case_id} удалена успешно.')
        else:
            print(f'Справа с ID {case_id} не найдена.')

    @staticmethod
    def create_case(category, name, name_eng, description, description_eng, masa, cena):
        session = Session()
        new_case = Case(name, name_eng, description, description_eng, masa, cena, category)
        if new_case:
            session.add(new_case)
            session.commit()
            session.close()

    @staticmethod
    def update_case(case_id, category, name, name_eng, description, description_eng, masa, cena):
        session = Session()
        user_to_update = session.query(Case).filter_by(id=case_id).first()

        if user_to_update:
            user_to_update.category = category
            user_to_update.name = name
            user_to_update.name_eng = name_eng
            user_to_update.description = description
            user_to_update.description_english = description_eng
            user_to_update.masa = masa
            user_to_update.price = cena

            session.commit()

            session.refresh(user_to_update)

        else:
            print("Пользователь с заданным идентификатором не найден.")

        session.close()

    def __repr__(self):
        return f' [{self.name} ID: {self.id}, state: {self.case_state}]'

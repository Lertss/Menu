from PySide6.QtWidgets import QMessageBox

from models.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from models.database import Session


class Case(Base):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    description_english = Column(String, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    masa = Column(Integer)
    case_state = Column(Integer, ForeignKey('case_state.id'))
    category = Column(Integer, ForeignKey('category.id'), nullable=False)

    def __init__(self, name: str = "", description: str = "",
                 description_english: str = "", price: str = "", masa: str = "", category: str = ""):
        self.name = name
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

        else:
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f'Danie z ID {case_id} nie znaleziono.')
            msgbox.exec()

            session.close()

    @staticmethod
    def create_case(category, name, description, description_eng, masa, cena):
        session = Session()
        new_case = Case(name, description, description_eng, masa, cena, category)
        if new_case:
            session.add(new_case)
            session.commit()
            session.close()
        else:
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText("Bląd stworzenia dania. *Case.create_case")
            msgbox.exec()

            session.close()

    @staticmethod
    def update_case(case_id, category, name, description, description_eng, masa, cena):
        session = Session()
        danie_to_update = session.query(Case).filter_by(id=case_id).first()

        if danie_to_update:
            danie_to_update.category = category
            danie_to_update.name = name

            danie_to_update.description = description
            danie_to_update.description_english = description_eng
            danie_to_update.masa = masa
            danie_to_update.price = cena

            session.commit()

            session.refresh(danie_to_update)
            session.close()
        else:
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f'Danie z ID {case_id} nie znaleziono *Case.update_case')
            msgbox.exec()
            session.close()

    def __repr__(self):
        return f' [{self.name} ID: {self.id}, state: {self.case_state}]'

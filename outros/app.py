from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///youth.db', echo=True)

Base = declarative_base()



class Contato(Base):
    __tablename__ = 'contatos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    celular = Column(String(20))
    email = Column(String(100))
    endereco = Column(String(100))


# Base.metadata.create_all(engine)

contato = Contato(nome='Juvenaldo', email='batchijuve@gmail.com', celular='997822831', endereco = 'rua de cima')


Session = sessionmaker(bind=engine)
session = Session()
session.add(contato)
session.commit()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///fake.db', echo=True)
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)

    nome = Column(String(100))
    idade = Column(Integer)
    endereco = Column(String(150))
    contato = Column(String(20))

class Veiculo(Base):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)

    nome = Column(String(30))
    marca = Column(String(30))
    capacidade_tanque = Column(Integer)
    cor = Column(String(30))
    ano_fabricacao = Column(Integer)


# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# for i in range(20):
#     pessoa = Pessoa(
#         nome=f'Pessoa {i}',
#         idade= 15+i,
#         endereco= f'Rua {i}, Cidade{i+2}',
#         contato= f'{i}{i+3}{i*3}{i+5}'
#     )
#     session.add(pessoa)

# for i in range(20):
#     veiculo = Veiculo(
#         nome=f'Veiculo {i}',
#         marca=f'Marca {i%5}',
#         capacidade_tanque= 40+i,
#         cor=f'Cor {i % 3}',
#         ano_fabricacao= 1997 + i
#     )

#     session.add(veiculo)

# contatos = session.query(Pessoa).all()
# # contatos = session.query(Pessoa).filter_by(nome='Pessoa 0')
# # contatos = session.query(Pessoa).filter(Pessoa.idade>20
# # contatos = session.query(Pessoa).filter(Pessoa.idade>20).filter(Pessoa.idade<30)
# # contatos = session.query(Pessoa).all()
# # contatos = session.query(Pessoa).filter_by(nome='Pessoa 0')
# # contatos = session.query(Pessoa).filter(Pessoa.idade>20)
# # contatos = session.query(Pessoa).filter(Pessoa.idade>20).filter(Pessoa.idade<30)

# contato = session.query(Pessoa).filter_by(nome='Pessoa 1').first()
# session.delete(contato)

# session.commit()

# for contato in contatos:
#     print(contato.nome)



# # for contato in contatos:
# #     print(contato.nome)



from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://vadim:password@localhost:3306/ormpy', echo=False)


Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Описуємо модель таблиці
class User(Base):
    __tablename__ = 'users'  # Назва таблиці

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Створення таблиці в базі даних
#Base.metadata.create_all(engine)
#student1 = User(name='John', age=12,id=1)
#student2 = User(name='Jan', age=15,id=2)
#student3 = User(name='Maria', age=14,id=3)
#session.add(student1)
#session.add_all([student2,student3])
#session.commit()
# Tralalelo tralala
#student = session.query(User).filter(User.age==14).first()
#print(student.name)

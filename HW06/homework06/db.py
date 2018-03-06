from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///news.db")  # создает новый экземпляр класса, который отвечает за подключение к бд
session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    link = Column(String)
    comments = Column(Integer)
    likes = Column(Integer)
    label = Column(String)


Base.metadata.create_all(bind=engine)


def save(prebase):
    s = session()
    is_label = s.query(News).filter(News.label == None).all()  # собираем новости без лейблов
    filter_news = []
    for j in is_label:
        filter_news.append(j.name)
    for i in prebase:
        if i['name'] not in filter_news:
            news = News(name=i['name'],
                        author=i['author'],
                        comments=i['comments'],
                        likes=i['likes'],
                        link=i['link'])
            s.add(news)
    s.commit()

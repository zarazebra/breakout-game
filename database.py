from sqlalchemy import create_engine, Column, Integer, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

engine = create_engine('sqlite:///highscores.db', echo=True)


class Base(DeclarativeBase):
    pass


class HighScore(Base):
    __tablename__ = "highscores"

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)


Base.metadata.create_all(engine)


class ScoreRepository:
    def __init__(self):
        self.session = Session(engine)

    def get_current_highscore(self):
        result = self.session.execute(select(HighScore).order_by(HighScore.score.desc()))
        highest_score = result.scalars().first()
        if highest_score is None:
            highest_score = 0
        return highest_score.score

    def add_new_highscore(self, score):
        new_highscore = HighScore(score=score)
        self.session.add(new_highscore)
        self.session.commit()

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped

engine = create_engine("sqlite+pysqlite:///memory:", echo=True)


class Base(DeclarativeBase):
    pass


class Score(Base):
    __tablename__ = "highscore"

    id: Mapped[int] = mapped_column(primary_key=True)
    highscore: Mapped[int] = mapped_column(ForeignKey("score"))


with Session(engine) as session:
    result = session.execute()
    session.commit()

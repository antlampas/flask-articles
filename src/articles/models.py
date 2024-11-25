from flask                    import current_app
from sqlalchemy.orm           import DeclarativeBase,MappedAsDataclass,Mapped,mapped_column
from datetime                 import datetime
from flask_admin.contrib.sqla import ModelView

class Base(DeclarativeBase, MappedAsDataclass):
    pass

class Article(current_app.database.Model):
    __tablename__ = "articles"
    title:            Mapped[str] = mapped_column(primary_key=True)
    content:          Mapped[str]
    author:           Mapped[str] = mapped_column(nullable=False)
    last_modified_by: Mapped[str] = mapped_column(nullable=False)
    created:          Mapped[str] = mapped_column(nullable=False)
    last_modified:    Mapped[str] = mapped_column(nullable=False)
    associate_page:   Mapped[str]

current_app.database.create_all()

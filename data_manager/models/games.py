from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional

from .. import constants
from .base import Base

class Games(Base):
    __tablename__ = constants.GAMES_TABLE_NAME

    id: Mapped[str] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column()
    done: Mapped[bool] = mapped_column(default=False)
    red_score: Mapped[Optional[int]] = mapped_column()
    green_score: Mapped[Optional[int]] = mapped_column()
    yellow_score: Mapped[Optional[int]] = mapped_column()
    blue_score: Mapped[Optional[int]] = mapped_column()
    grey_score: Mapped[Optional[int]] = mapped_column()
    purple_score: Mapped[Optional[int]] = mapped_column()
    orange_score: Mapped[Optional[int]] = mapped_column()
    pink_score: Mapped[Optional[int]] = mapped_column()

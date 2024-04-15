from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import BaseClass


class Donation(BaseClass):
    user_id = Column(Integer, ForeignKey('user.id', name='fk_donation_user_id_user'))
    comment = Column(Text)
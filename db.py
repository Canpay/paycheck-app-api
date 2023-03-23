from typing import List, Optional
import databases
import ormar
import sqlalchemy

database = databases.Database("postgresql://mcano:pjNxOLD176uhFPHwcziCtvUmrXoL2QVL@dpg-cgbkm9hmbg55nqmr6klg-a.oregon-postgres.render.com/paycheck")
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
"""
class PlaceOpeningHoursPeriodDetail(ormar.Model):
    class Meta

class PlaceOpeningHoursPeriod(ormar.Model):
    class Meta(BaseMeta):
        tablename = "place_opening_hours_period"
    
    open: 
    close: 

class PlaceOpeningHours(ormar.Model):
    class Meta(BaseMeta):
        tablename = "place_opening_hours"

    id: int = ormar.Integer(primary_key=True)
    periods: Optional[List[Period]] = ormar.ManyToMany(Period)
    special_days:
    weekday_text:
"""

class Place(ormar.Model):
    class Meta(BaseMeta):
        tablename = "place"

    id: int = ormar.Integer(primary_key=True)
    formatted_address: str = ormar.String(max_length=80)
    formatted_phone_number: str = ormar.String(max_length=20)
    name: str = ormar.String(max_length=80)
    rating: float = ormar.Float(precision=1)
    user_ratings_total: int = ormar.Integer(nullable=False)
    price_level: int = ormar.Integer(nullable=False)
    types: str = ormar.String(max_length=100)
    editorial_summary: str = ormar.String(max_length=200)
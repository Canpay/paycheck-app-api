from typing import List, Optional
import databases
import ormar
import sqlalchemy

#database = databases.Database("postgresql://mcano:pjNxOLD176uhFPHwcziCtvUmrXoL2QVL@dpg-cgbkm9hmbg55nqmr6klg-a.oregon-postgres.render.com/paycheck")
database = databases.Database("postgres://mcano:pjNxOLD176uhFPHwcziCtvUmrXoL2QVL@dpg-cgbkm9hmbg55nqmr6klg-a/paycheck")

metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata

class Place(ormar.Model):
    class Meta(BaseMeta):
        tablename = "place"

    id: int = ormar.Integer(primary_key=True)
    formatted_address: str = ormar.String(max_length=80)
    postal_code: int = ormar.Integer(nullable=False)
    town: str = ormar.String(max_length=50)
    province: str = ormar.String(max_length=50)
    location: str = ormar.String(max_length=20)
    formatted_phone_number: str = ormar.String(max_length=20)
    name: str = ormar.String(max_length=80)
    rating: float = ormar.Float(precision=1)
    user_ratings_total: int = ormar.Integer(nullable=False)
    price_level: int = ormar.Integer(nullable=False)
    types: str = ormar.String(max_length=100)
    editorial_summary: str = ormar.String(max_length=200)
    up_gourmet_check: bool = ormar.Boolean(nullable=False)
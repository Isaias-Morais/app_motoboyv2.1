from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost/motoboy_finacias"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

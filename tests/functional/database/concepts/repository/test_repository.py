from sqlalchemy import select

from database.concepts import repository


class TestRepository:
    def test_correctly_gets_engine(self):
        engine = repository.Repository.get_engine()

        assert engine is not None

    def test_correctly_executes_simple_query(self):
        result = repository.Repository.run(select(1)).fetchall()

        assert result == [
            (1,),
        ]

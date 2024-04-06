import pytest
import sqlalchemy
from sqlalchemy import select, text

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


class TestTransactional:
    ############
    # FIXTURES #
    ############

    @pytest.fixture(scope="function")
    def prepare_database(self):
        repository.Repository.run(
            text(
                """
                    CREATE TABLE table_for_tests(
                        id INT PRIMARY KEY
                    );
                """
            ),
        )

        yield

        repository.Repository.run(
            text(
                """
                    DROP TABLE table_for_tests;
                """
            ),
        )

    #########
    # TESTS #
    #########

    def test_correctly_inserts_for_no_exceptions(
        self,
        prepare_database,
    ):
        self.correct_insert(tx=None)

        result = self.get_result()

        assert len(result) == 1
        assert result[0] == (1,)

    def test_does_not_insert_with_exception(
        self,
        prepare_database,
    ):
        try:
            self.insert_with_exception(tx=None)
        except Exception:
            pass

        result = self.get_result()

        assert len(result) == 0

    def test_does_not_inserts_partly(
        self,
        prepare_database,
    ):
        try:
            self.insert_correct_and_with_exception(tx=None)
        except Exception:
            pass

        result = self.get_result()

        assert len(result) == 0

    ###########
    # HELPERS #
    ###########

    @repository.transactional
    def correct_insert(
        self,
        tx: sqlalchemy.Connection,
    ):
        repository.Repository.run(
            text(
                """
                INSERT INTO table_for_tests
                (id) VALUES (1);
                """
            ),
            tx=tx,
        )

    @repository.transactional
    def insert_with_exception(
        self,
        tx: sqlalchemy.Connection,
    ):
        repository.Repository.run(
            text(
                """
                INSERT INTO table_for_tests
                (id) VALUES (2);
                """
            ),
            tx=tx,
        )
        raise Exception("ooooops")

    @repository.transactional
    def insert_correct_and_with_exception(
        self,
        tx: sqlalchemy.Connection,
    ):
        self.correct_insert(tx=tx)
        self.insert_with_exception(tx=tx)

    @staticmethod
    def get_result() -> list:
        result = repository.Repository.run(
            text(
                """
                SELECT *
                FROM table_for_tests;
                """
            ),
        )
        return result.fetchall()

from decimal import Decimal

import pytest

from common.concepts import random
from common.constants import ID_LENGTH


class TestGenerateId:
    def test_ok(self):
        result = random.generate_id()

        assert type(result) is str
        assert len(result) == ID_LENGTH


class TestGenerateString:
    @pytest.mark.parametrize(
        "length",
        [
            3,
            5,
            15,
        ],
    )
    def test_ok(self, length):
        result = random.generate_string(
            length=length,
        )

        assert type(result) is str
        assert len(result) == length


class TestGenerateInt:
    @pytest.mark.parametrize(
        "mi, ma",
        [
            (5, 5),
            (7, 10),
            (100, 150),
            (200, 250),
            (50, 75),
        ],
    )
    def test_ok(self, mi, ma):
        result = random.generate_int(
            min=mi,
            max=ma,
        )

        assert type(result) is int
        assert mi <= result <= ma


class TestGenerateDecimal:
    @pytest.mark.parametrize(
        "mi, ma",
        [
            (Decimal("0"), Decimal("0.5")),
            (5, 5),
            (7, 10),
            (100, 150),
            (200, 250),
            (50, 75),
        ],
    )
    def test_ok(self, mi, ma):
        result = random.generate_decimal(
            min=mi,
            max=ma,
        )

        assert type(result) is Decimal
        assert mi <= result <= ma

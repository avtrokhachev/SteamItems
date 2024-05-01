from decimal import Decimal

import pytest

from worker.src.functions import convert_to_dollars


class TestConvertToDollars:
    @pytest.mark.parametrize(
        "raw_price, expected_price",
        [
            ["$1.22", Decimal("1.22")],
            ["1.22$", Decimal("1.22")],
            [" $1.22  ", Decimal("1.22")],
            ["$50,55", Decimal("50.55")],
            ["100$", Decimal("100")],
        ],
    )
    def test_ok(self, raw_price: str, expected_price: Decimal):
        price = convert_to_dollars(raw_price)

        assert price == expected_price

    def test_raises_exception_on_incorrect_price(self):
        raw_price = "12,55"

        with pytest.raises(Exception):
            convert_to_dollars(raw_price)

import copy
import unittest

from exporter import render_orders


class RenderOrdersTests(unittest.TestCase):
    def test_filter_sort_columns_escaping_and_input_preservation(self):
        orders = [
            {"id": 10, "status": "open", "note": 'comma, "quote"\nnext', "amount": 0},
            {"id": 1, "status": "closed", "note": "excluded"},
            {"id": 2, "status": "open", "note": None},
        ]
        original = copy.deepcopy(orders)
        self.assertEqual(
            render_orders(orders, ["note", "id", "amount"], status="open"),
            'note,id,amount\n,2,\n"comma, ""quote""\nnext",10,0\n',
        )
        self.assertEqual(orders, original)

    def test_no_filter_and_descending_numeric_sort(self):
        orders = [{"id": 2, "status": "open"}, {"id": 10, "status": "closed"}]
        self.assertEqual(render_orders(orders, ["id"], descending=True), "id\n10\n2\n")

    def test_empty_status_is_supplied_filter(self):
        orders = [{"id": 1, "status": "open"}, {"id": 2, "status": ""}]
        self.assertEqual(render_orders(orders, ["id"], status=""), "id\n2\n")

    def test_no_matches_keeps_header(self):
        self.assertEqual(render_orders([{"id": 1, "status": "open"}], ["id", "status"], status="OPEN"), "id,status\n")
        self.assertEqual(render_orders([], ["id"]), "id\n")


if __name__ == "__main__":
    unittest.main()

"""Render local order records using the accepted CSV export contract."""

import csv
import io


def render_orders(orders, columns, status=None, descending=False):
    rows = (order for order in orders if status is None or order["status"] == status)
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(columns)
    for order in sorted(rows, key=lambda order: order["id"], reverse=descending):
        writer.writerow(order.get(column) for column in columns)
    return output.getvalue()

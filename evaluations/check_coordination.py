"""Acceptance checks for an implementation of coordination-fixture/TASK.md."""
import copy
import csv
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def check(root):
    spec = importlib.util.spec_from_file_location('candidate_exporter', root / 'exporter.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    records = [
        {'id': 10, 'status': 'open', 'note': 'hello, "world"', 'private': 'omit'},
        {'id': 2, 'status': 'closed', 'note': None},
        {'id': 3, 'status': 'open', 'note': 'two\nlines'},
        {'id': 1, 'status': 'open'},
    ]
    original = copy.deepcopy(records)
    parse = lambda text: list(csv.reader(io.StringIO(text)))
    render = module.render_orders
    text = render(records, ['note', 'id'], status='open', descending=True)
    assert parse(text) == [['note', 'id'], ['hello, "world"', '10'], ['two\nlines', '3'], ['', '1']]
    assert '\r' not in text and text.endswith('\n')
    assert parse(render(records, ['id'])) == [['id'], ['1'], ['2'], ['3'], ['10']]
    assert parse(render(records, ['id', 'note'], status='closed')) == [['id', 'note'], ['2', '']]
    assert parse(render(records, ['id'], status='missing')) == [['id']]
    assert records == original
    with tempfile.TemporaryDirectory() as directory:
        source = Path(directory) / 'orders.json'
        source.write_text(json.dumps(records), encoding='utf-8')
        before = source.read_bytes()
        result = subprocess.run([sys.executable, str(root / 'cli.py'), str(source),
                                 '--columns', 'note', 'id', '--status', 'open', '--descending'],
                                capture_output=True, text=True, cwd=directory, timeout=10)
        assert result.returncode == 0, result.stderr
        assert result.stdout == text and result.stderr == ''
        assert source.read_bytes() == before
        assert sorted(p.name for p in Path(directory).iterdir()) == ['orders.json']
    print('Export contract and combined CLI acceptance checks passed.')


if __name__ == '__main__':
    check(Path(sys.argv[1]).resolve())

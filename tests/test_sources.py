"""检查离线资料的格式、引用和业务时点。"""
from pathlib import Path
import unittest

from inspect_inputs import read_table


DATA = Path(__file__).resolve().parents[1] / "data"
FIELDS = {
    'index_notices': ['notice', 'known', 'effective', 'weights'],
    'opening_portfolio': ['asset', 'units'],
    'security_calendar': ['asset', 'day', 'open_utc', 'close_utc', 'lot', 'max_volume', 'lower', 'upper'],
    'corporate_actions': ['action', 'asset', 'kind', 'known', 'record', 'ex_day', 'pay_day', 'rate'],
    'quotes': ['id', 'asset', 'for_day', 'known', 'price', 'revises'],
    'execution_tape': ['fill', 'day', 'time', 'asset', 'side', 'shares', 'price', 'fee', 'settle'],
    'sessions': ['day', 'decision_utc', 'nav_utc', 'benchmark_level'],
}


class InputBundleTest(unittest.TestCase):
    def test_csv_contract(self):
        self.assertEqual({p.stem for p in DATA.glob("*.csv")}, set(FIELDS))
        for name, expected in FIELDS.items():
            with self.subTest(table=name):
                fields, rows = read_table(DATA, name)
                self.assertEqual(fields, expected)
                self.assertTrue(rows)
                self.assertTrue(all(None not in row and None not in row.values() for row in rows))

    def test_related_source_records(self):
        _, records = read_table(DATA, 'index_notices')
        notices = {row['notice']: row for row in records}
        _, records = read_table(DATA, 'corporate_actions')
        actions = {row['action']: row for row in records}
        _, records = read_table(DATA, 'sessions')
        slots = {row['day']: row for row in records}
        _, records = read_table(DATA, 'execution_tape')
        fills = {row['fill']: row for row in records}
        self.assertGreater(notices['I2']['known'], '2026-05-18T07:00:00Z')
        self.assertEqual(actions['CA1']['ex_day'], slots['2026-05-18']['day'])
        self.assertGreater(actions['CA2']['pay_day'], fills['F4']['day'])


if __name__ == "__main__":
    unittest.main()

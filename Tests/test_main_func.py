from main import check_row
import pytest


@pytest.mark.parametrize('row, expected',
                         [('(((([{}]))))', 'Balanced'),
                          ('[([])((([[[]]])))]{()}', 'Balanced'),
                          ('{{[()]}}', 'Balanced'),
                          ('', 'Unbalanced'),
                          (' ', 'Unbalanced'),
                          ('}{}', 'Unbalanced'),
                          ('{{[(])]}}', 'Unbalanced'),
                          ('[[{())}]', 'Unbalanced')])
def test_rows(row, expected):
    assert check_row(row) == expected

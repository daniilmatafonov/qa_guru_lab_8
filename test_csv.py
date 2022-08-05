import csv

path = 'unpacked/movies.csv'


def test_read_csv_():
    with open(path) as f:
        reader = csv.reader(f)
        headers = next(reader)
    assert 'Film' in str(headers)
    assert 'Genre' in str(headers)
    assert 'Lead' in str(headers)
    assert 'Studio' in str(headers)
    assert 'Audience score %' in str(headers)
    assert 'Profitability' in str(headers)
    assert 'Rotten Tomatoes %' in str(headers)
    assert 'Worldwide Gross' in str(headers)
    assert 'Year' in str(headers)

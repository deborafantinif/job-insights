from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    list_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert list_jobs[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }

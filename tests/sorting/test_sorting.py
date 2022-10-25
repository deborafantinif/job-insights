from src.sorting import sort_by

list_jobs = [
    {
        "min_salary": 10,
        "max_salary": 800,
        "date_posted": "2021-02-21"
    },
    {
        "min_salary": 5,
        "max_salary": 700,
        "date_posted": "2021-02-25"
    },
    {
        "min_salary": 30,
        "max_salary": 500,
        "date_posted": "2021-02-22"
    }
]

order_by_min_salary = [
    {
        "min_salary": 5,
        "max_salary": 700,
        "date_posted": "2021-02-25"
    },
    {
        "min_salary": 10,
        "max_salary": 800,
        "date_posted": "2021-02-21"
    },
    {
        "min_salary": 30,
        "max_salary": 500,
        "date_posted": "2021-02-22"
    }
]

order_by_max_salary = [
    {
        "min_salary": 10,
        "max_salary": 800,
        "date_posted": "2021-02-21"
    },
    {
        "min_salary": 5,
        "max_salary": 700,
        "date_posted": "2021-02-25"
    },
    {
        "min_salary": 30,
        "max_salary": 500,
        "date_posted": "2021-02-22"
    }
]

order_by_date_posted = [
    {
        "min_salary": 5,
        "max_salary": 700,
        "date_posted": "2021-02-25"
    },
    {
        "min_salary": 30,
        "max_salary": 500,
        "date_posted": "2021-02-22"
    },
    {
        "min_salary": 10,
        "max_salary": 800,
        "date_posted": "2021-02-21"
    },
]


def test_sort_by_criteria():
    assert sort_by(list_jobs, "min_salary") == order_by_min_salary
    assert sort_by(list_jobs, "max_salary") == order_by_max_salary
    assert sort_by(list_jobs, "date_posted") == order_by_date_posted

import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_array = [job for job in jobs]

    return jobs_array

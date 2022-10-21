from src.jobs import read


def get_unique_job_types(path):
    jobs_array = read(path)
    type_of_jobs = set()
    for job in jobs_array:
        type_of_jobs.add(job["job_type"])
    type_of_jobs_array = [job for job in type_of_jobs]
    return type_of_jobs_array


def filter_by_job_type(jobs, job_type):
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type


def get_unique_industries(path):
    jobs_array = read(path)
    industry = set()
    for job in jobs_array:
        if job["industry"] != "":
            industry.add(job["industry"])
    industry_array = [job for job in industry]
    return industry_array


def filter_by_industry(jobs, industry):
    jobs_by_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_by_industry


def get_max_salary(path):
    jobs_array = read(path)
    salaries = set()
    for job in jobs_array:
        if job["max_salary"] != "" and not job["max_salary"].isalpha():
            salaries.add(int(job["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    jobs_array = read(path)
    salaries = set()
    for job in jobs_array:
        if job["min_salary"] != "" and not job["min_salary"].isalpha():
            salaries.add(int(job["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError
    elif (type(job['min_salary']) != int) or (type(job['max_salary']) != int):
        raise ValueError
    elif type(salary) != int or job['min_salary'] > job['max_salary']:
        raise ValueError
    else:
        return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        range = {
            "min_salary": job["min_salary"],
            "max_salary": job["max_salary"]
        }
        try:
            if matches_salary_range(range, salary):
                result.append(job)
        except ValueError as err:
            print(err)
    return result

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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

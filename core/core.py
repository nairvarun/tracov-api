import requests
from bs4 import BeautifulSoup


def main():
    worldometer = "https://www.worldometers.info/coronavirus/"
    source = requests.get(worldometer)
    page = BeautifulSoup(source.text, "lxml")

    # index = [
    #     i.text.strip()
    #     for i in page.select(
    #         "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(1)"
    #     )
    # ]
    country = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(2)"
        )
    ]
    total_cases = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(3)"
        )
    ]
    new_cases = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(4)"
        )
    ]
    total_deaths = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(5)"
        )
    ]
    new_deaths = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(6)"
        )
    ]
    total_recovered = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(7)"
        )
    ]
    new_recovered = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(8)"
        )
    ]
    active_cases = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(9)"
        )
    ]
    critical_cases = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(10)"
        )
    ]
    tot_cases_per_mil = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(11)"
        )
    ]
    deaths_per_mil = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(12)"
        )
    ]
    total_tests = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(13)"
        )
    ]
    tests_per_mil = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(14)"
        )
    ]
    population = [
        i.text.strip()
        for i in page.select(
            "#main_table_countries_today > tbody:nth-child(2) > tr > td:nth-child(15)"
        )
    ]

    data = {
        i[0]: dict(
            zip(
                (
                    "total_cases",
                    "new_cases",
                    "total_deaths",
                    "new_deaths",
                    "total_recovered",
                    "new_recovered",
                    "active_cases",
                    "critical_cases",
                    "tot_cases_per_mil",
                    "deaths_per_mil",
                    "total_tests",
                    "tests_per_mil",
                    "population",
                ),
                list(i[1:]),
            )
        )
        for i in zip(
            country,
            total_cases,
            new_cases,
            total_deaths,
            new_deaths,
            total_recovered,
            new_recovered,
            active_cases,
            critical_cases,
            tot_cases_per_mil,
            deaths_per_mil,
            total_tests,
            tests_per_mil,
            population,
        )
    }

    return data


if __name__ == "__main__":
    main()

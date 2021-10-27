# todo:
    # turn this into a proper module
    # publish at pypi
    # instead of scraping every time, get the whole thing at the beging and then scrape that?? idk if that better or worse 
    # add comments and documentation
    # add license

# region imports
import requests
from bs4 import BeautifulSoup
import cupdater
#endregion

# region class

class Location:

    def __init__(self, name):
        self.name = name
        Location.get_info(self, name)

    def get_info(self, name):
        url = 'https://www.worldometers.info/coronavirus/#countries'

        source = requests.get(url).text

        soup = BeautifulSoup(source, 'lxml')

        table = soup.find('table', id='main_table_countries_today')

        country = name
        tbody = table.tbody.find_all('td')        
        c = 0
        is_counting = False
        get_popu = False
        country_data = []
        for i in tbody:
            if i.string == country:
                is_counting = True
            if is_counting:
                country_data.append(i.string)
                c += 1
            if c >=15:
                break

        for i in table.tbody.find_all('a', href=True): 
            if i.text == country:
                get_popu = True
            if get_popu == True:
                x = i.attrs
                if len(x) == 1:
                    country_data.append(i.string)
                    break

        if name == 'World':
            self.total_cases = country_data[1]
            self.new_cases = country_data[2]
            self.total_deaths = country_data[3]
            self.new_deaths = country_data[4]
            self.total_recovered = country_data[5]
            self.new_recovered = country_data[6]
            self.active_cases = country_data[7]
            self.critical_cases = country_data[8]
            self.cases_per_mil = country_data[9]
            self.deaths_per_mil = country_data[10]

        elif name in ['North America', 'Asia', 'South America', 'Europe', 'Africa', 'Australia/Oceania']:
            table_data = table.tbody.find_all('tr', class_='total_row_world row_continent')
            is_counting = False
            continent_data = []
            temp_list = []
            continent = name
            for i in table_data:
                td_tags = i.findAll('td')
                for j in td_tags:
                    if j.string != None:
                        temp_list.append(j.text)
                        if j.string == continent:
                            if j.string == 'South America':
                                continent_data = temp_list[-6:-1]
                                self.total_cases = continent_data[0]
                                self.total_deaths = continent_data[1]
                                self.total_recovered = continent_data[2]
                                self.active_cases = continent_data[3]
                                self.critical_cases = continent_data[4]
                                break
                            else:
                                continent_data = temp_list[-9:-1]
                                self.total_cases = continent_data[0]
                                self.new_cases = continent_data[1]
                                self.total_deaths = continent_data[2]
                                self.new_deaths = continent_data[3]
                                self.total_recovered = continent_data[4]
                                self.new_recovered = continent_data[5]
                                self.active_cases = continent_data[6]
                                self.critical_cases = continent_data[7]
                                break

        else:
            self.total_cases = country_data[1]
            self.new_cases = country_data[2]
            self.total_deaths = country_data[3]
            self.new_deaths = country_data[4]
            self.total_recovered = country_data[5]
            self.new_recovered = country_data[6]
            self.active_cases = country_data[7]
            self.critical_cases = country_data[8]
            self.cases_per_mil = country_data[9]
            self.deaths_per_mil = country_data[10]
            self.total_tests = country_data[11]
            self.tests_per_mil = country_data[12]
            self.continent = country_data[14]
            self.population = country_data[15]

    def get_list(param):
        url = 'https://www.worldometers.info/coronavirus/#countries'

        source = requests.get(url).text

        soup = BeautifulSoup(source, 'lxml')

        table = soup.find('table', id='main_table_countries_today')


        table_data = table.tbody.find_all('tr')
        country_list = []
        continent_list = ['North America', 'Asia', 'South America', 'Europe', 'Africa', 'Australia/Oceania']
        full_list = ['world']

        for i in range(len(table_data)):
            try:
                # getting main countries
                key = table_data[i].find_all('a', class_='mt_a')[0].string
                # print(key)
                country_list.append(key)
            except:
                try:
                    # getting weird countries
                    key = table_data[i].find('td', style="font-weight: bold; font-size:15px; text-align:left;").string
                    country_list.append(key)
                except:
                    pass
        
        full_list = full_list + continent_list + country_list
        
        if param == 'all':
            return full_list
        elif param == 'countries':
            return country_list
        elif param == 'continents':
            return continent_list
        else:
            return None


# endregion

# region function definitions

# region main function 

def main():
    pass

# endregion

if __name__ == '__main__':
    main()
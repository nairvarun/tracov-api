# todo:
    # turn cupdater into a proper module that can be installed by anyone.
    # find out a way to make the 'bot request: BAD' reply look good.
    # add docs

#region imports
import cupdater
import praw
import login
#endregion

# region function definitions

# gets data from cupdater and prepares the reply
def get_data(location):
    
    c19 = cupdater.Location(location)

    if location == 'World':
        total_cases = c19.total_cases
        new_cases = c19.new_cases
        total_deaths = c19.total_deaths
        new_deaths = c19.new_deaths
        total_recovered = c19.total_recovered
        new_recovered = c19.new_recovered
        active_cases = c19.active_cases
        critical_cases = c19.critical_cases
        cases_per_mil = c19.cases_per_mil
        deaths_per_mil = c19.deaths_per_mil

        # use '/n' twice for it to be properly displayed on reddit.
        reply = (
        '{loc}: \n\n'
        'total cases = {total_cases}\n\n'
        'new cases = {new_cases}\n\n'
        'total deaths = {total_deaths}\n\n'
        'new deaths = {new_deaths}\n\n'
        'total recovered = {total_recovered}\n\n'
        'new recovered = {new_recovered}\n\n'
        'active cases = {active_cases}\n\n'
        'critical cases = {critical_cases}\n\n'
        'cases per million = {cases_per_mil}\n\n'
        'deaths per million = {deaths_per_mil}'
        ).format(
            loc = location,
            total_cases = total_cases, 
            new_cases = new_cases, 
            total_deaths = total_deaths, 
            new_deaths = new_deaths, 
            total_recovered = total_recovered, 
            new_recovered = new_recovered, 
            active_cases = active_cases, 
            critical_cases = critical_cases, 
            cases_per_mil = cases_per_mil, 
            deaths_per_mil = deaths_per_mil
            )

    elif location in ['North America', 
    'Asia', 'South America', 'Europe', 'Africa', 'Australia/Oceania']:
        if location == 'South America':
            total_cases = c19.total_cases
            total_deaths = c19.total_deaths
            total_recovered = c19.total_recovered
            active_cases = c19.active_cases
            critical_cases = c19.critical_cases
        
            # use '/n' twice for it to be properly displayed on reddit.
            reply = (
            '{loc}: \n\n'
            'total cases = {total_cases}\n\n'
            'total deaths = {total_deaths}\n\n'
            'total recovered = {total_recovered}\n\n'
            'active cases = {active_cases}\n\n'
            'critical cases = {critical_cases}'
            ).format(
                loc = location,
                total_cases = total_cases, 
                total_deaths = total_deaths, 
                total_recovered = total_recovered, 
                active_cases = active_cases, 
                critical_cases = critical_cases, 
                )

        else:
            total_cases = c19.total_cases
            new_cases = c19.new_cases
            total_deaths = c19.total_deaths
            new_deaths = c19.new_deaths
            total_recovered = c19.total_recovered
            new_recovered = c19.new_recovered
            active_cases = c19.active_cases
            critical_cases = c19.critical_cases

            # use '/n' twice for it to be properly displayed on reddit.
            reply = (
            '{loc}: \n\n'
            'total cases = {total_cases}\n\n'
            'new cases = {new_cases}\n\n'
            'total deaths = {total_deaths}\n\n'
            'new deaths = {new_deaths}\n\n'
            'total recovered = {total_recovered}\n\n'
            'new recovered = {new_recovered}\n\n'
            'active cases = {active_cases}\n\n'
            'critical cases = {critical_cases}'
            ).format(
                loc = location,
                total_cases = total_cases, 
                new_cases = new_cases, 
                total_deaths = total_deaths, 
                new_deaths = new_deaths, 
                total_recovered = total_recovered, 
                new_recovered = new_recovered, 
                active_cases = active_cases, 
                critical_cases = critical_cases, 
                )

    else:
        total_cases = c19.total_cases
        new_cases = c19.new_cases
        total_deaths = c19.total_deaths
        new_deaths = c19.new_deaths
        total_recovered = c19.total_recovered
        new_recovered = c19.new_recovered
        active_cases = c19.active_cases
        critical_cases = c19.critical_cases
        cases_per_mil = c19.cases_per_mil
        deaths_per_mil = c19.deaths_per_mil
        total_tests = c19.total_tests
        tests_per_mil = c19.tests_per_mil
        continent = c19.continent
        population = c19.population

        reply = (
        '{loc}: \n\n'
        'total cases = {total_cases}\n\n'
        'new cases = {new_cases}\n\n'
        'total deaths = {total_deaths}\n\n'
        'new deaths = {new_deaths}\n\n'
        'total recovered = {total_recovered}\n\n'
        'new recovered = {new_recovered}\n\n'
        'active cases = {active_cases}\n\n'
        'critical cases = {critical_cases}\n\n'
        'cases per million = {cases_per_mil}\n\n'
        'deaths per million = {deaths_per_mil}\n\n'
        'total tests = {total_tests}\n\n'
        'tests per million = {tests_per_mil}\n\n'
        'continent = {continent}\n\n'
        'population = {population}'
        ).format(
            loc = location,
            total_cases = total_cases, 
            new_cases = new_cases, 
            total_deaths = total_deaths, 
            new_deaths = new_deaths, 
            total_recovered = total_recovered, 
            new_recovered = new_recovered, 
            active_cases = active_cases, 
            critical_cases = critical_cases, 
            cases_per_mil = cases_per_mil, 
            deaths_per_mil = deaths_per_mil,
            total_tests = total_tests,
            tests_per_mil = tests_per_mil,
            continent = continent,
            population = population
            )
    
    return reply

# starts the bot 
def run_bot(reddit):

    for item in reddit.inbox.stream():
        req = [i for i in item.body.split(' ')]
        valid_locations = cupdater.Location.get_list('all')
        username = 'u/'+login.username
        if req[0] == username and req[1] in valid_locations:
            print('bot request: OK')

            r = get_data(req[1])

            item.reply(str(r))
            print('reply: OK')

            item.mark_read()
            print('mark as read: OK')
        else:
            print('bot request: BAD')

            # find out a way to make this reply look good.
            item.reply(str(sorted(valid_locations)))
            print('reply: OK')

            item.mark_read()
            print('mark as read: OK')

        # uncomment 'break' if you want the bot to only run once
        # break

# main function
def main():

    reddit = praw.Reddit(client_id = login.client_id,
                        client_secret = login.client_secret,
                        username = login.username,
                        password = login.password,
                        user_agent = login.user_agent) 

    if reddit.user.me() == login.username:
        print('authentication: OK')
    else:
        print('authentication: FAILED')

    run_bot(reddit)

# endregion

if __name__ == '__main__':
    main()

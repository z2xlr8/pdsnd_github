import time
import math
import pandas as pd
import numpy as np

#define dictionaries
city_dic = { "Chicago": "data/chicago.csv",
              "New York City": "data/new_york_city.csv",
              "Washington": "data/washington.csv" }

month_dic = { "january": 1,
                "february": 2,
                "march": 3,
                "april": 4,
                "may": 5,
                "june": 6,
                "jan": 1,
                "feb": 2,
                "mar": 3,
                "apr": 4,
                "may": 5,
                "jun": 6, 
                "all": "all"}

week_dic = { "monday": 0,
                "tuesday": 1,
                "wednesday": 2,
                "thursday": 3,
                "friday": 4,
                "saturday": 5,
                "sunday": 6, 
                "all": "all"}

yay_nay_dic = {"yes": True, 
                "no": False}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('-'*40)
    
    print('Hello! Let\'s explore some US bikeshare data!\n\n(Please enter number or type the option as shown)\n')
    
    print('-'*40)
    
    # TO DO: get user input for city (Chicago, New York City, Washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please select one of the following cities:\n(1) Chicago\n(2) New York City\n(3) Washington\nGet data for: ").lower()
            
            """ convert numerical option data to alpha numeric equivalent """
            if city == '1':
                city = 'chicago'
            elif city == '2':
                city = 'new york city'
            elif city == '3':
                city = 'washington'
           
            city = city.title()
      
        except KeyboardInterrupt:
            print("\nTerminated by user.\n")
            raise

        if city not in city_dic:
            print("Sorry, not a valid option.\n")
        else:
            break

    print('-'*40)
    
    # TO DO: get user input for month (all, January, February, ... , June)
    while True:
        try:
            month = input("\nSelect one of the first six months of the year:\n(1) Jan\n(2) Feb\n(3) Mar\n(4) Apr\n(5) May\n(6) Jun\n(7) All, to select the first six months of the year\nGet data for: ").lower()
 
            """ convert numerical option data to alpha numeric equivalent """
            if month == 'jan' or month == '1':
                month = 'january'
            elif month == 'feb' or month == '2':
                month = 'february'
            elif month == 'mar' or month == '3':
                month = 'march'
            elif month == 'apr' or month == '4':
                month = 'april'
            elif month == 'may' or month == '5':
                month = 'may'
            elif month == 'jun' or month == '6':
                month = 'june'
            elif month == '7':
                month = 'all'

        except KeyboardInterrupt:
            print("\nTerminated by user.\n")
            raise
        if month not in month_dic:
            print("Sorry, not a valid option.\n")
        else:
            break

    print('-'*40)
    
    # TO DO: get user input for day of week (all, Monday, Tuesday, ... Sunday)
    while True:
        try:
            day = input("\nSelect a day of the week:\n(1) Sunday\n(2) Monday\n(3) Tuesday\n(4) Wednesday\n(5) Thursday\n(6) Friday\n(7) Saturday\n(8) All, to select the entire week\nGet data for: ").lower()
 
            """ convert numerical option data to alpha numeric equivalent """
            if day == 'sun' or day == '1':
                day = 'sunday'
            elif day == 'mon' or day == '2':
                day = 'monday'
            elif day == 'tue' or day == 'tues' or day == '3':
                day = 'tuesday'
            elif day == 'wed' or day == '4':
                day = 'wednesday'
            elif day == 'thur' or day == '5':
                day = 'thursday'
            elif day == 'fri' or day == '6':
                day = 'friday'
            elif day == 'sat' or day == '7':
                day = 'saturday'
            elif day == 'all' or day == '8':
                day = 'all'
            
        except KeyboardInterrupt:
            print("\nTerminated by user.\n")
            raise
        if day not in week_dic:
            print("Sorry, not a valid option.\n")
        else:
            break
        
        day = week_dic[day]
        
    print('-'*40)
    
    #city_str, month_str, day_str - used to provide decriptive data in results
    city_str = city.title()
    month_str = month.title()
    day_str = day.title()
    
    #city, month, day - used in data analysis
    city = city_dic[city]
    month = month_dic[month]
    day = week_dic[day]

    return city, month, day, city_str, month_str, day_str

#-----------------------------------------------------------------------------------------------

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    if day != 'all':
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]
    df.drop('day_of_week', axis = 1, inplace=True)
    df.drop('month', axis = 1, inplace=True)
    return df

#-----------------------------------------------------------------------------------------------

def time_stats(df, city_str, month_str, day_str):
    """Displays statistics on the most frequent times of travel."""
    
    most_freq_hour = ''

    print('\nCalculating The Most Frequent Times of Travel in {}...\n'.format(city_str))
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month

    #displays data for all months and days of the week
    if month_str == 'All' and day_str == 'All':
        
        # TO DO: display the most common month
        most_freq_month = df['month'].mode()[0]
        for num in month_dic:
            if month_dic[num] == most_freq_month:
                most_freq_month = num.title()
        print('Most popular month for travel is {}'.format(most_freq_month))
        
        # TO DO: display the most common day of week
        most_freq_day = df['day_of_week'].mode()[0]
        for num in week_dic:
            if week_dic[num] == most_freq_day:
                most_freq_day = num.title()
        print('Most popular day of week for travel is {}'.format(most_freq_day))

        # TO DO: display the most common start hour
        df['hour']=pd.to_datetime(df['Start Time']).dt.hour
        most_freq_hour = convert_hour_am_pm(df['hour'].mode()[0])
        print('Most popular hour to begin travel is {}.'.format(most_freq_hour))
    
    #displays data for a specific month and all days of the week
    elif month_str != 'All' and day_str == 'All':
    
        # TO DO: display the most common day of week for a given month
        most_freq_day = df['day_of_week'].mode()[0]
        for num in week_dic:
            if week_dic[num]==most_freq_day:
                most_freq_day = num.title()
        print('For the month of {} the most popular day of week for travel is {}'.format(month_str, most_freq_day))

       # TO DO: display the most common start hour
        df['hour']=pd.to_datetime(df['Start Time']).dt.hour
        most_freq_hour = convert_hour_am_pm(df['hour'].mode()[0])
        print('Most popular hour to begin travel is {}.'.format(most_freq_hour))
    
    #displays data for all months and a specific day of the week
    elif month_str == 'All' and day_str != 'All':
    
        # TO DO: display the most common month on a given day
        most_freq_month = df['month'].mode()[0]
        for num in month_dic:
            if month_dic[num]==most_freq_month:
                most_freq_month = num.title()
        print('On {} the most popular month for travel is {}'.format(day_str, most_freq_month))
        
       # TO DO: display the most common start hour
        df['hour']=pd.to_datetime(df['Start Time']).dt.hour
        most_freq_hour = convert_hour_am_pm(df['hour'].mode()[0])
        print('Most popular hour to begin travel is {}.'.format(most_freq_hour))
    
    #displays data for a specific month and day of the week
    else:

       # TO DO: display the most common start hour
        df['hour']=pd.to_datetime(df['Start Time']).dt.hour
        most_freq_hour = convert_hour_am_pm(df['hour'].mode()[0])
        print('For the month of {} on {}, the most popular hour to begin travel is {}.'.format(month_str, day_str, most_freq_hour))

    df.drop('hour', axis = 1, inplace = True)
    df.drop('day_of_week', axis = 1, inplace = True)
    df.drop('month', axis = 1, inplace = True)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------------------

def convert_hour_am_pm(hour):
    """converts from 24 hour format and adds AM or PM to provide a more decriptive hour output"""
    
    if hour > 12:
        hour = hour - 12
        if hour == 0:
            time_output = 'Midnight'
        else:
            time_output = str(hour) + ' PM'
    elif hour == 0:
        time_output = 'Midnight'
    else:
        time_output = str(hour) + ' AM'
        
    return time_output

#-----------------------------------------------------------------------------------------------

def station_stats(df, city_str):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trips for {}...\n'.format(city_str))
    start_time = time.time()

    # TO DO: display most commonly used start station
    print()
    print('Most commonly used start station in {} is {}'.format(city_str, df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print()
    print('Most commonly used end station in {} is {}'.format(city_str, df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print()
    most_freq_station_comb = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequent combination of start station and end station (trip) in {} is {}'.format(city_str, most_freq_station_comb.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------------------

def trip_duration_stats(df, city_str):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration Information for {}...\n'.format(city_str))
    start_time = time.time()
    travel_durations = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # TO DO: display total travel time
    print()
    td_sum = df['Trip Duration'].sum()
    ttl_sec = td_sum % 60
    ttl_min = td_sum // 60 % 60
    ttl_hr = td_sum // 3600 % 60
    ttl_days = td_sum // 24 // 3600
    print('Total usage was {} days, {} hours, {} minutes and {} seconds'.format(ttl_days, ttl_hr, ttl_min, ttl_sec))

    # TO DO: display mean travel time
    print()
    td_mean = math.ceil(df['Trip Duration'].mean())
    avg_sec = td_mean % 60
    avg_min = td_mean // 60 % 60
    avg_hr = td_mean // 3600 % 60
    avg_days = td_mean // 24 // 3600
    print('Average travel time: {} hours, {} minutes and {} seconds'.format(avg_hr, avg_min, avg_sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------------------

def user_stats(df, city_str):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats for {}...\n'.format(city_str))
    start_time = time.time()

    # TO DO: Display counts of user types
    print()
    types_of_usrs = df.groupby('User Type', as_index = False).count()
    print('There are {} types of users.'.format(len(types_of_usrs)))
    for i in range(len(types_of_usrs)):
        print('{}\'s - {} total'.format(types_of_usrs['User Type'][i], types_of_usrs['Start Time'][i]))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print('No gender data available.')
    else:
        gndr_of_usrs = df.groupby('Gender', as_index = False).count()
        print('Number of user genders in {}: {}'.format(city_str, len(gndr_of_usrs)))
        for i in range(len(gndr_of_usrs)):
            print('{}s - {}'.format(gndr_of_usrs['Gender'][i], gndr_of_usrs['Start Time'][i]))
        print('There is no gender data available for the {} users in {}.'.format(len(df) - gndr_of_usrs['Start Time'][0] - gndr_of_usrs['Start Time'][1], city_str))

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    if 'Birth Year' not in df:
        print('Birth year data is not available for {}.'.format(city_str))
    else:
        birth = df.groupby('Birth Year', as_index = False).count()
        print('For {}.'.format(city_str))
        print('Earliest year of birth was {}.'.format(int(birth['Birth Year'].min())))
        print('Most recent year of birth was {}.'.format(int(birth['Birth Year'].max())))
        print('Most common year of birth year was {}.'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------------------------------------------

def display_data(df, city_str):
    choice = input('Would you like to read some of the raw data for {}? (Y)es or (N)o '.format(city_str)).lower()
    print()
    
    if choice == "y":
        choice = "yes"
    elif choice == "n":
        choice = "no"
                
    if choice in yay_nay_dic:
        choice = yay_nay_dic[choice]
    else:
        print('You did not enter a valid choice. Please try that again.')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Do wish to seee another five results for {}? (Y)es or (N)o '.format(city_str)).lower()
            
            if choice == "y":
                choice = "yes"
            elif choice == "n":
                choice = "no"
                        
            if choice in yay_nay_dic:
                choice = yay_nay_dic[choice]
            else:
                print('You did not enter a valid choice. Please try that again.')
                display_data(df)
                return
            
            if choice == True:
                continue
            elif choice == False:
                break
            else:
                print('You did not enter a valid choice.')
                return

#-----------------------------------------------------------------------------------------------

def main():
    while True:
        end_cntr = 0
        
        city, month, day, city_str, month_str, day_str = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city_str, month_str, day_str)
        station_stats(df, city_str)
        trip_duration_stats(df, city_str)
        user_stats(df, city_str)
        display_data(df, city_str)
        
        #ask user if they want to continue
        continue_or_surrender()

#-----------------------------------------------------------------------------------------------

def continue_or_surrender():

    end_cntr = 0
    
    while True:
        try:
        
            restart = input('\nRestart analysis? Please enter (Y)es or (N)o.\n').lower()
            
            if restart == "y":
                restart = "yes"
            elif restart == "n":
                restart = "no"

        except KeyboardInterrupt:
            print("\nTerminated by user.\n")
            raise
        
        #terminate if no valid option is chosen more than 5 consecutive times
        if restart not in yay_nay_dic:
            print("Sorry, not a valid option.\n")
            if end_cntr >= 5:
                print("\nObviously you are done. Bye.\n")
                quit()
            else:
                end_cntr += 1
        else:
            
            if restart == 'yes' or restart == 'y':
                print("\nLet go again.\n")
                break
            else:
                print("\nThank you, bye.\n")
                quit()



if __name__ == "__main__":
    main()


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Input the name of one of the following cities: Chicago, New york city or Washington. ').lower()
            if city in CITY_DATA.keys():
                break
            else:
                print('Sorry, {} is not a valid city'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
        except Exception as e:
            print("Exception occurred: {}".format(e))
    while True:
        month = input('Input name of the month (all, january, february, ... , june). ').lower()
        if month == 'all' or month in months:
            break
        else:
            print('Sorry, {} is not a month in the data'.format(month))

    while True:
        day = input('Input name of the weekday (all, monday, tuesday, ... sunday). ').lower()
        if day == 'all' or day in days:
            break
        else:
            print('Sorry, {} is not a valid day'.format(day))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day

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
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}'.format(int(df.mode()['month'][0])))


    # TO DO: display the most common day of week
    print('The most common day of the week is: {}'.format(df.mode()['day_of_week'][0]))


    # TO DO: display the most common start hour
    print('The most common start hour is: {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: {}'.format(df['Start Station'].value_counts().keys()[0]))


    # TO DO: display most commonly used end station
    print('The most commonly used end station is: {}'.format(df['End Station'].value_counts().keys()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + ' - ' + df['End Station']
    commom_route = df['Route'].value_counts().keys()[0]
    print('The most frequent combination of start station and end station trip is: {}'.format(commom_route))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: {} seconds'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('The mean travel time is: {} seconds'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count of user type is: {}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('The count of Gender is: {}'.format(df['Gender'].value_counts()))
    else:
        print()

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The earlist year of birth is: {}'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth is: {}'.format(int(df['Birth Year'].max())))
        print('The most common year of birth is: {}'.format(int(df['Birth Year'].value_counts().keys()[0])))
    else:
        print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    while True:
        display = input('\nWould you like to see raw data? Enter yes or no.\n')
        if display.lower() != 'yes':
            break
        else:
            n = 0
            print(df.iloc[n:n+5])
            more_data = input('\nWould you like to see the next 5 rows? Enter yes or no.\n')
            if more_data.lower() != 'yes':
                break
            else:
                n += 5
                print(df.iloc[n:n+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

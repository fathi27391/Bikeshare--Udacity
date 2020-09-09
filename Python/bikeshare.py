import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# List of abbreviated cities that can be entered instead of full name
city_short = { 'ch': 'chicago',
              'ny': 'new york city',
              'nyc': 'new york city',
              'wa': 'washington' }

# All month data ( Full month and abbreviated - 3 letter format-)
month_data = { 'january': 1,
              'february': 2,
              'march': 3,
              'april': 4 ,
              'may': 5,
              'june': 6,
              'jan=': 1,
              'feb': 2,
              'mar=': 3,
              'apr': 4 ,
              'may': 5,
              'jun': 6}

# All days data from monday to sunday ( Default in weeday function: Monday = 0)
day_data = { 'monday': 'Monday',
              'mon': 'Monday',
              'tuesday': 'Tuesday',
              'tue': 'Tuesday',
              'wednesday': 'Wednesday',
              'wed': 'Wednesday',
              'thrusday=': 'Thrusday',
              'thr': 'Thrusday',
              'friday=': 'Friday',
              'fri': 'Friday',
              'saturday': 'Saturday',
              'sat': 'Saturday',
              'sunday': 'Sunday',
              'sun': 'Sunday'}

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
        city = input('Please Enter a City name :[Chicago/ch], [New york city/ny], [Washington/wa] to analyze?  ').lower()
        if city in CITY_DATA:
            city = CITY_DATA[city]
            print()
            break
        elif city in city_short:
            city = city_short[city]
            city = CITY_DATA[city]
            print()
            break
        else:
            print('Would you please Enter a Valid city Name . . Let\'s try again')
            print()

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('How do want to filter you data by month .. Select [all] if you don\'t want to filter')
        month = input('Choose: all, January/jan, February/feb, March/mar, April/apr, May/may, June/jun ?  ').lower()
        if month == 'all':
            month = 'all'
            print()
            break
        elif month in month_data:
            month = month_data[month]
            print()
            break
        else:
            print("Kindly Enter a valid Month to continue, type [all] if you want to include all months . . Let\'s try again")
            print()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('How do want to filter you data by day of the week .. Select all if you don\'t want to filter')
        day = input('Choose: all, Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun?  '      ).lower()
        if day == 'all':
            day = 'all'
            print()
            break
        elif day in day_data:
            day = day_data[day]
            print()
            break
        else:
            print("Kindly Enter a valid day to continue, type [all] if you want to include all days of the week")
            print()

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
     # Orginial data stored according to user inputs
    df= pd.read_csv(city)
    # Add new column for month and weekday name
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
     # filter by month if chosen
    if month != 'all':
        df = df.loc[df['month'] == month]
    else:
        df.drop(['month'], axis=1, inplace=True)
    # Filter by weekday if applicable
    if day != 'all':
        df = df.loc[df['weekday'] == day.title()]
    else:
        df.drop(['weekday'], axis=1, inplace=True)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Add new column for month and weekday name
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    for key, value in month_data.items():
        if value == common_month:
            common_month_name = key
    print("The most common month for bicyle renting is : {}".format(common_month_name))

    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    print("The most common Day of the week for bicyle renting is : {}".format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common Hour for bicyle renting is the {} hr".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print()
    common_start_st = df['Start Station'].mode()[0]
    print('The most common start station is : {}'.format(common_start_st))

    # TO DO: display most commonly used end station
    print()
    common_end_st = df['End Station'].mode()[0]
    print('The most common end station in bike renting is : {}'.format(common_end_st))

    # TO DO: display most frequent combination of start station and end station trip
    print()
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('The most common trip for bike renting in the filtered data is: {}'.format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print()
    total_time = df['Trip Duration'].sum()

    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    # how many days, hours and minutes
    days = total_time // seconds_in_day
    hours = (total_time - (days * seconds_in_day)) // seconds_in_hour
    minutes = (total_time - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute

    print('Total Duration of the trip is {} days, {} hours, {} minutes'.format(days, hours, minutes))
    # TO DO: display mean travel time
    print()
    mean_time = df['Trip Duration'].mean()
    mean_time_min = round((mean_time/60),2)
    print('The mean travel time for bike renting in filtered data is {} minutes'.format(mean_time_min))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Use of the Build-in method value_counts to count the unique values there

    print()
    print("Display the distribution of filtered data according to User Type")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # Use of the Build-in method value_counts to count the unique values there
    print()
    try:
        print("The distribution of filtered data according to Gender")
        print(df['Gender'].value_counts())
    except KeyError:
        print("No Gender Column Available in the dataset")

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    print("Birth Year statistics in the data: ")
    try:
        old_year = int(df['Birth Year'].min())
        new_y = int(df['Birth Year'].max())
        com_yr = int(df['Birth Year'].mode()[0])
        print('{} is the earliest birth year , while {} is the most recent, {} is the most common one'.format(old_year, new_y, com_yr))
    except KeyError:
        print("There is NO Birth Year column available in the Data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    while True:
        print()
        choice = input('Would you like to see row data ? Yes/y or No/n     ').lower()
        print()
        i = 0
        while choice == 'yes' or choice == 'y':
            df_part = df.iloc[i:i+5]
            print(df_part)
            i += 5
            choice_2 = input('Would you like more data to view? Yes/y or No/n..     ').lower()
            if choice_2 == 'no' or choice_2 == 'n':
                break
        
        if choice == 'no' or choice == 'n' or choice_2 == 'n' or choice_2 == 'no':
            break
        else:
            print('Please Enter a valid answer . . Let\'s try again')




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

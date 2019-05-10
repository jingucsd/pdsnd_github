import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Would you like to see data for Chicago, New York City, or Washington\n").lower()
    while city not in ["chicago", "new york city", "washington"]:
            city = input("Would you like to see data for Chicago, New York, or Washington\n").lower()
    time_filter = input("Would you like to filter the data by month, day, both or not at all? Type 'none' for no time filter.\n")
    while time_filter.lower() not in ["month", "day", "both", "none"]:
        time_filter = input("Would you like to filter the data by month, day, both or not at all? Type 'none' for no time filter.\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    month = "all"
    if time_filter in ["month", "both"]:
        month = input("Which month - January, February, March, April, May, or June?\n").lower()
        while month not in ["all", "january", "february", "march", "april", "may", "june"]:
            month = input("Which month - January, February, March, April, May, or June?\n").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = "all"
    if time_filter in ["day", "both"]:
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
        while day not in ["all","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
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
    #practice solution #3
    
    # use the city parameter and the CITY_DATA dictionary to select the correct csv file to read
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # practice problem/solution #1
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    print("most common month: {}".format(months[popular_month+1]))

    popular_day = df['day_of_week'].mode()[0] 
    print("most popular day: {}".format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("most popular hour: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common start station: {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most common end station: {}".format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    # group dataframe by start and end station columns
    grouped_dataframe = df.groupby(['Start Station', 'End Station']) 
    most_common_group = grouped_dataframe.size().nlargest(1) # size() returns the size of each group. nlargest(1) gets largest out of groupby object
    print("Most common combo: {}".format(most_common_group))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("total travel time: {}".format(total_travel))

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("mean travel time: {}".format(mean_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Practice problem/solution #2
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("user types:{}".format(user_types))


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("genders: {}".format(gender))
    else:
        print("no gender data in dataset\n")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthyear = df['Birth Year'].min()
        mostRecent_birthyear = df['Birth Year'].max()
        mostCommon_birthyear = df['Birth Year'].mode()[0]
        print("Earliest birth year: {}, Most recent birth year: {}, Most comon birth year: {}".format(earliest_birthyear, mostRecent_birthyear, mostCommon_birthyear))
    else:
        print("No birth year data in dataset\n")
            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    show_raw_data = input('Would you like to see the raw data? Enter yes or no.\n')
    idx = 0
    while show_raw_data.lower() == 'yes' and idx + 5 < len(df.index):
        print(df.iloc[idx:idx + 5])
        idx += 5
        show_raw_data = input('Would you like to see 5 more rows of raw data? Enter yes or no.\n')
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

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

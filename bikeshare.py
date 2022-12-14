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
    
    city = input("Enter the city name \n").lower()
    while city != "chicago" and city != "new york city" and city != "washington":
        city = input("please enter one of chicago, new york city, washington").lower()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    month = input("insert month from('january', 'february', 'marh', 'april', 'may', 'june', 'all')\n").lower()
    months= ('january', 'february', 'marh', 'april', 'may', 'june')
    while month != 'all' and month not in months:
        print("please reinsert a valid month")
  
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("insert a day\n").lower()
    days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all')
    while day not in days:
        day = input("please insert a day").lower()
            
    

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Start hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = ('january', 'february', 'marh', 'april', 'may', 'june')
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month is : {}".format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print("the most common day is : {}".format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print("the most common start hour is : {}".format(df['Start hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly start station : {}".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print("the most commonly end station : {}".format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station']+","+df['End Station']
    print("the most frequent trip is : {}".format(df['trip'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time : {}".format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print("average travel time : {}".format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())


    # TO DO: Display counts of gender
    print(df['Gender'].value_counts().to_frame())
    


    # TO DO: Display earliest, most recent, and most common year of birth
    print("the earliest year of birth is : {}".format(int(df['Birth Year'].min())))
    print("the most recent year of birth is : {}".format(int(df['Birth Year'].max())))
    print("the most common year of birth is : {}".format(int(df['Birth Year'].mode()[0])))
    
                                                   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print("Data is ready\n")
    i = 0
    user_input = input("would you like to display 5 lines of data? please insert yes or no\n").lower()
    if user_input not in ['yes', 'no']:
        print("sorry please type yes or no")
        user_input = input("would you like to display 5 lines of data? please insert yes or no\n").lower()
    elif user_input != 'yes':
        print("thanks")
    else:
        while i + 5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            user_input = input("would you live to display 5 more data lines ?\n").lower()
            if user_input != 'yes':
                print("thanks")
                break
            
           
        
        
    
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

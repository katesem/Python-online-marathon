def check_day_week(day):
    try:
        week = {
                1: 'Monday',
                2: 'Tuesday',
                3: 'Wednesday',
                4: 'Thursday',
                5: 'Friday',
                6: 'Saturday',
                7: 'Sunday'
                }
        
        if not isinstance(day,int):
            raise TypeError("You did not enter a number!Please try again.")
        
        elif not 0 < day < 7 :
            raise ValueError("There is no such day of the week!Please try again.")
        else:
            print(week[day])
            
    except (Exception) as e:
        print(e)
        

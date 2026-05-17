def add_time(start, duration, day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parse start time
    time_part, period = start.split()
    start_hours, start_minutes = map(int, time_part.split(':'))
    dur_hours, dur_minutes = map(int, duration.split(':'))

    # Convert to 24-hour total minutes
    if period == 'PM' and start_hours != 12:
        start_hours += 12
    if period == 'AM' and start_hours == 12:
        start_hours = 0

    total_minutes = start_hours * 60 + start_minutes + dur_hours * 60 + dur_minutes

    final_hours = (total_minutes // 60) % 24
    final_minutes = total_minutes % 60
    days_later = total_minutes // (60 * 24)

    # Convert back to 12-hour format
    if final_hours == 0:
        result_period = 'AM'
        display_hours = 12
    elif final_hours < 12:
        result_period = 'AM'
        display_hours = final_hours
    elif final_hours == 12:
        result_period = 'PM'
        display_hours = 12
    else:
        result_period = 'PM'
        display_hours = final_hours - 12

    result = f'{display_hours}:{final_minutes:02d} {result_period}'

    # Add day of week
    if day:
        start_day_index = days_of_week.index(day.capitalize())
        result_day = days_of_week[(start_day_index + days_later) % 7]
        result += f', {result_day}'

    # Add days later label
    if days_later == 1:
        result += ' (next day)'
    elif days_later > 1:
        result += f' ({days_later} days later)'

    return result
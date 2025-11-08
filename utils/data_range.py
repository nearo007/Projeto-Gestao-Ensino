from datetime import date

today = date.today()

def get_age_range():
    min_year = today.year - 80
    max_year = today.year - 18

    min_date = date(min_year, 1, 1).isoformat()
    max_date = date(max_year, 12, 31).isoformat()
    
    age_range = [min_date, max_date]
    
    return age_range

def get_assignment_range():
    min_date = date(today.year, today.month, today.day).isoformat()
    max_date = date(today.year, 12, 31).isoformat()
    
    data_range = [min_date, max_date]
    
    return data_range
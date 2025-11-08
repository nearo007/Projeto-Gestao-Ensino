from datetime import date

def get_age_range():
    today = date.today()

    min_year = today.year - 80
    max_year = today.year - 18

    min_date = date(min_year, 1, 1).isoformat()
    max_date = date(max_year, 12, 31).isoformat()
    
    age_range = [min_date, max_date]
    
    return age_range
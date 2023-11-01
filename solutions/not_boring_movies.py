import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema.query("id % 2 == 1 & description != 'boring'").sort_values(by='rating', ascending=False)
    

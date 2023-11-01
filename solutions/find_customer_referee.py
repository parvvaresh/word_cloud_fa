import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(customer.query("referee_id != 2 | referee_id.isna()")["name"])


    

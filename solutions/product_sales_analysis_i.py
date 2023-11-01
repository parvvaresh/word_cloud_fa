import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales.join(product.set_index("product_id"), on="product_id").dropna()[["product_name" , "year" , "price"]]    

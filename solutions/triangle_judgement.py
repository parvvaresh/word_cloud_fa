import pandas as pd

def check(df):
    if df.x + df.y > df.z and df.y + df.z > df.x and df.x + df.z > df.y:
        return "Yes"
    return "No"

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle.apply(check, axis=1)
    return triangle

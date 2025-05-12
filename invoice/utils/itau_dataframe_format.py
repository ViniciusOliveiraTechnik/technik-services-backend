import pandas as pd

from accounts.utils import time_performance

@time_performance(detail_name="itau_dataframe_format")
def itau_dataframe_format(dataframe: pd.DataFrame):

    pattern_name = r'[A-Za-zÀ-ÿ\s\-]+FINAL\s+[0-9\*]+'

    invoice = dataframe.iloc[:, [0, 2, 10]].copy()
    invoice.columns = ['purchase_date', 'description', 'value']

    invoice['converted_purchase_date'] = pd.to_datetime(invoice['purchase_date'], format="%Y-%m-%d %H:%M:%S", errors='coerce')
    has_card_name = invoice['purchase_date'].astype(str).str.match(pattern_name, na=False)

    invoice['card'] = invoice['purchase_date'].where(has_card_name).str.extract(r'^([A-Za-zÀ-ÿ\s\-]+)\s-\sFINAL')[0].ffill()

    invoice = invoice[invoice['converted_purchase_date'].notna()].drop(columns='converted_purchase_date').reset_index(drop=True)
    
    invoice[['installment', 'installments']] = invoice['description'].str.extract(r'(\d{2})/(\d{2})').astype(float).astype('Int64')

    invoice['installment'] = invoice['installment'].fillna(1)
    invoice['installments'] = invoice['installments'].fillna(1)

    return invoice.to_dict(orient='records')

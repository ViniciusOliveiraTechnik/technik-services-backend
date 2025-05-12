import pandas as pd
import time

from invoice.utils import itau_dataframe_format
from invoice.serializers import InvoiceDataSerializer

from accounts.models import Account
from accounts.utils import time_performance

@time_performance(detail_name="process_invoice_file")
def process_invoice_file(file, user: Account):

    try:

        start = time.time()

        df = pd.read_excel(file)

        end = time.time()

        print(end - start)

    except Exception as err:
        
        raise ValueError(f'Erro ao ler o arquivo: {err}')

    try:

        invoice_data = itau_dataframe_format(df) # Call dataframe manipulation
        
    except Exception as err:
        raise ValueError(f'Erro ao formatar dados: {err}')

    start = time.time()
    serializer = InvoiceDataSerializer(data=invoice_data, many=True)
    serializer.is_valid(raise_exception=True)
    serializer.save(created_by=user)
    end = time.time()

    print(end - start)

    return serializer.data

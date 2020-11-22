from openpyxl import load_workbook
from db import process_db
from model.ErrorData import OracleErrorData
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
excel_path = os.path.join(cur_dir, 'dataset.xlsx')


def save_dataset(kind):
    # 엑셀파일 로드
    # print(excel_path)
    load_wb = load_workbook(excel_path, data_only=True)
    if kind == 'oracle_error':
        oracle_err_sheet = load_wb['oracle_data']

        oracle_err_dataset = []
        for row in oracle_err_sheet.rows:
            oracle_err_data = []
            for cell in row:
                if cell.value is not None:
                    oracle_err_data.append(cell.value[:len(cell.value) - 1])
                else:
                    oracle_err_data.append(cell.value)

            if oracle_err_data[0] is not None and oracle_err_data[0].startswith('ORA'):
                oracle_err_dataset.append(oracle_err_data)

        # DB에 데이터셋 저장
        result = process_db.insert_dataset(kind, oracle_err_dataset)

        return result


def load_dataset(kind):
    if kind == 'oracle_error':
        oracle_err_dataset = process_db.load_dataset(kind)
        oracle_errzip = dict()
        for data in oracle_err_dataset:
            oracle_errzip[data['error_code']] = OracleErrorData(data['error_code'],
                                                                data['situation'],
                                                                data['cause'],
                                                                data['description'],
                                                                data['solution'])

        return oracle_errzip
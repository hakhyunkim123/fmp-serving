from openpyxl import load_workbook
from db import process_db
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
excel_path = os.path.join(cur_dir, 'dataset.xlsx')

class OracleErrorData:
    def __init__(self):
        self.situation = ''
        self.cause = ''
        self.description = ''
        self.solution = ''
        self.error_code = ''

    def __init__(self, error_code, situation, cause, description, solution):
        self.error_code = error_code
        self.situation = situation
        self.cause = cause
        self.description = description
        self.solution = solution

    def set_data(self, col, data):
        if col == '현상':
            self.situation += data
        elif col == '원인':
            self.cause += data
        elif col == '조치':
            self.solution += data
        elif col == 'code':
            self.error_code += data
        elif col == 'kor_desc':
            self.description += data

    def set_errcode(self, errcode_list):
        error_code = ''
        description = ''
        for code, desc in errcode_list.items():
            error_code += code + '\n'
            description += desc + '\n'

        self.error_code = error_code
        self.description = description

    def reset(self):
        self.situation = ''
        self.cause = ''
        self.description = ''
        self.solution = ''
        self.error_code = ''

    def to_dict(self):
        # self.print_data()
        return {
            'error_code': self.error_code,
            'situation': self.situation,
            'description': self.description,
            'cause': self.cause,
            'solution': self.solution
        }

    def print_data(self):
        print('====================================================')
        print('situation:', self.situation.encode('utf-8'))
        print('cause:', self.cause.encode('utf-8'))
        print('solution:', self.solution.encode('utf-8'))
        print('description:', self.description.encode('utf-8'))
        print('error_code:', self.error_code.encode('utf-8'))


#         print('====================================================')

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
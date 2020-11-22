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
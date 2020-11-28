class User:
    def __init__(self, employ_num=None, name=None, email=None, position=None,
                 comp_division=None, comp_division_detail=None, pwd=None, user_dict=None):
        if user_dict is None:
            self.employ_num = employ_num
            self.name = name
            self.email = email
            self.position = position
            self.comp_division = comp_division
            self.comp_division_detail = comp_division_detail
            self.pwd = pwd
        else:
            self.employ_num = user_dict['employ_num']
            self.name = user_dict['name']
            self.email = user_dict['email']
            self.position = user_dict['position']
            self.comp_division = user_dict['comp_division']
            self.comp_division_detail = user_dict['comp_division_detail']
            self.pwd = user_dict['pwd']

    def to_dict(self):
        user_to_dict = {
            'employ_num': self.employ_num,
            'name': self.name,
            'email': self.email,
            'position': self.position,
            'comp_division': self.comp_division,
            'comp_division_detail': self.comp_division_detail
        }

        return user_to_dict

    def print_user_info(self):
        print('행번:', self.employ_num)
        print('이름:', self.name)
        print('이메일:', self.email)
        print('직급:', self.position)
        print('부서:', self.comp_division)
        print('팀:', self.comp_division_detail)

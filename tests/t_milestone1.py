import sys
from pathlib import Path

PROJECT_ROOT= Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

# 从tool包中导入函数
from tools.hr_tools import get_employee_profile,check_leave_balance,generate_employment_certificate

if __name__ == '__main__':
    print('-------测试1：查看 张三的档案-----------')
    print(get_employee_profile.invoke({'uid':'1001'}))

    print('----------测试2：查看 李四的假期余额---------')
    print(check_leave_balance.invoke({'uid':'1002'}))

    print('----------测试3：查看 张三的收入证明---------')
    print(generate_employment_certificate.invoke({'uid':'1001','cert_type':'income'}))

    print('----------测试4：查看 李四的收入证明---------')
    print(generate_employment_certificate.invoke({'uid':'1002','cert_type':'income'}))


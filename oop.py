from employee import Employee,Manager

omar = Employee('Omar','Hossam','Developer',1000)
# omar.info()

yasin = Manager('Yasin','Hasanin','Team Lead',100000,[omar])
khaled = Employee('Khaled','Elsayed','Team Lead',10000)
yasin.team.append(khaled)
yasin.team.remove(khaled)
# yasin.emps_info()

# E.generate_emp(str) , M.generate_mang(str)
Employee.total_emps
Manager.total_mangs

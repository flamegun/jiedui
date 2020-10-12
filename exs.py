 while i < exp_num:
            random_num_operation = randint(1, config.max_num_of_oper)
            is_need_parenteses = randint(0,1)
            number_of_oprand = random_num_operation + 1 #操作数比操作符的数目多1
            exp = []
            for j in range(random_num_operation + number_of_oprand):
                if j % 2 == 0:
                    #随机生成操作数
                    exp.append(self.generate_operand(randint(0,3), config.num_range))
                    if j > 1 and exp[j-1] == '÷' and exp[j] == '0':
                        while True:
                            exp[j-1] = self.generate_operation()
                            if exp [j-1] == '÷':
                                continues
                            else:
                                break
                else:
                    #生成运算符
                    exp.append(self.generate_operation())

 if is_need_parenteses and number_of_oprand != 2:
                expression = " ".join(self.generate_parentheses(exp, number_of_oprand))
            else:
                expression = " ".join(exp)
            
            #判断是否有重复
            if self.is_repeat(exp_list, expression) or suffix_to_value(to_suffix(expression)) == False:
                continue
            else:
                exp_list.append(expression)
                i = i + 1
                if exp:
            exp_length = len(exp)
            left_position = randint(0,int(num/2))
            right_position = randint(left_position+1, int(num/2)+1)
            mark = -1
            for i in range(exp_length):
                if exp[i] in ['+', '-', 'x', '÷']:
                    expression.append(exp[i])
                else:
                    mark += 1
                    if mark == left_position:
                        expression.append('(')
                        expression.append(exp[i])
                    elif mark == right_position:
                        expression.append(exp[i])
                        expression.append(')')
                    else:
                        expression.append(exp[i])
        #如果生成的括号表达式形如 (1 + 2/3 + 3) 则重新生成
        if expression[0] == '(' and expression[-1] ==')':
            expression = self.generate_parentheses(exp, number_of_oprand)
            return expression

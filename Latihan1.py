# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi penambahan
def add(a, b):
    return a + b

# def tree(expr):
#     if isinstance(expr, tuple):
#         left, operator, right = expr
#         if operator == '+':
#             return add(tree(left), tree(right))
#         elif operator == '-':
#             return minus(tree(left), tree(right))
#         elif operator == '*':
#             return mult(tree(left), tree(right))
#     else:
#         return expr
    

def tree(node):
        if type(node) is tuple and len(node) == 3:
            left_operand, operator, right_operand = node
            if operator == '+':
                return tree(left_operand) + tree(right_operand)
            elif operator == '-':
                return tree(left_operand) - tree(right_operand)
            elif operator == '*':
                return tree(left_operand) * tree(right_operand)
            elif operator == '/':
                return tree(left_operand) / tree(right_operand)
        else:
            return node    


# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)
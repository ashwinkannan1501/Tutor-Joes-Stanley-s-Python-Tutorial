print("-------------------------------------------------- Normal Addition ------------------------------")
# Addition
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print(f'{a} + {b} = {a + b}')

print("----------------------------------------- Normal String Concatenation ----------------------------")
# String Concatenation
string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ")
print(f'{string1} + {string2} = {string1 + string2}')

print("-------------------------------------------- Normal Multiplication ------------------------")
# Multiplication
print(f'{a} * {b} = {a * b}')

print("--------------------------------------------- Normal String Repetition ----------------------------")
# String Repetition

print(f'{string1} * {a} = {a * string1}')


class Addition:
    def __init__(self, addition):
        self.addition = addition

    def __add__(self, other):
        return self.addition + other.addition


print("------------------------ User defined addition ------------------------------------")
obj1 = Addition(a)
obj2 = Addition(b)
print(f'{obj1.addition} + {obj2.addition} = {obj1 + obj2}')

print("---------------------- User defined string concatenation ------------------------------------")
obj1 = Addition(string1)
obj2 = Addition(string2)
print(f'{obj1.addition} + {obj2.addition} = {string1 + string2}')


class Subtraction:
    def __init__(self, subtraction):
        self.subtraction = subtraction

    def __sub__(self, other):
        return self.subtraction - other.subtraction


print("----------------------- User defined subtraction --------------------------------------")
obj1 = Subtraction(a)
obj2 = Subtraction(b)
print(f'{obj1.subtraction} - {obj2.subtraction} = {obj1 - obj2}')


class Multiplication:
    def __init__(self, multiplication):
        self.multiplication = multiplication

    def __mul__(self, other):
        return self.multiplication * other.multiplication


print("--------------------- User defined multiplication ---------------------------------")
obj1 = Multiplication(a)
obj2 = Multiplication(b)
print(f'{obj1.multiplication} * {obj2.multiplication} = {obj1 * obj2}')

print("------------------------- User defined string repetition ----------------------------------")
obj1 = Multiplication(string2)
obj2 = Multiplication(b)
print(f'{obj1.multiplication} * {obj2.multiplication} = {obj1 * obj2}')


class Division:
    def __init__(self, division):
        self.division = division

    def __truediv__(self, other):
        return self.division / other.division


print("----------------------------------- User Defined Division ---------------------------")
obj1 = Division(a)
obj2 = Division(b)
print(f"{obj1.division} / {obj2.division} = {obj1 / obj2}")


class Modulus:
    def __init__(self, modulus):
        self.modulus = modulus

    def __mod__(self, other):
        return self.modulus % other.modulus


print("------------------------------------ User Defined Modulus --------------------------------")
obj1 = Modulus(a)
obj2 = Modulus(b)
print(f'{obj1.modulus} % {obj2.modulus} = {obj1 % obj2}')


class IntegerDivision:
    def __init__(self, integer_division):
        self.integer_division = integer_division

    def __floordiv__(self, other):
        return self.integer_division // other.integer_division


print("--------------------------------- User Defined Integer Division ------------------------------")
obj1 = IntegerDivision(a)
obj2 = IntegerDivision(b)
print(f"{obj1.integer_division} // {obj2.integer_division} = {obj1 // obj2}")


class Power:
    def __init__(self, power):
        self.power = power

    def __pow__(self, other):
        return self.power ** other.power


print("----------------------------- User Defined Power (or) Exponential --------------------------")
obj1 = Power(a)
obj2 = Power(b)
print(f'{obj1.power} ** {obj2.power} = {obj1 ** obj2}')


class LesserThan:
    def __init__(self, lesser_than):
        self.lesser_than = lesser_than

    def __lt__(self, other):
        return self.lesser_than < other.lesser_than


print("---------------------------- Lesser Than (<) ---------------------------")
obj1 = LesserThan(a)
obj2 = LesserThan(b)
print(f'{obj1.lesser_than} < {obj2.lesser_than} = {obj1 < obj2}')


class LesserThanOrEqualTo:
    def __init__(self, lesser_than_or_equal_to):
        self.lesser_than_or_equal_to = lesser_than_or_equal_to

    def __le__(self, other):
        return self.lesser_than_or_equal_to <= other.lesser_than_or_equal_to


obj1 = LesserThanOrEqualTo(a)
obj2 = LesserThanOrEqualTo(b)
print(f'{obj1.lesser_than_or_equal_to} <= {obj2.lesser_than_or_equal_to} = {obj1 <= obj2}')


class GreaterThan:
    def __init__(self, greater_than):
        self.greater_than = greater_than

    def __gt__(self, other):
        return self.greater_than > other.greater_than


obj1 = GreaterThan(a)
obj2 = GreaterThan(b)
print(f'{obj1.greater_than} > {obj2.greater_than} = {obj1 > obj2}')


class GreaterThanOrEqualTo:
    def __init__(self, greater_than_or_equal_to):
        self.greater_than_or_equal_to = greater_than_or_equal_to

    def __ge__(self, other):
        return self.greater_than_or_equal_to >= other.greater_than_or_equal_to


obj1 = GreaterThanOrEqualTo(a)
obj2 = GreaterThanOrEqualTo(b)
print(f'{obj1.greater_than_or_equal_to} >= {obj2.greater_than_or_equal_to} = {obj1 >= obj2}')


class EqualTo:
    def __init__(self, equal_to):
        self.equal_to = equal_to

    def __eq__(self, other):
        return self.equal_to == other.equal_to


obj1 = EqualTo(a)
obj2 = EqualTo(b)
print(f'{obj1.equal_to} == {obj2.equal_to} = {obj1 == obj2}')


class NotEqualTo:
    def __init__(self, not_equal_to):
        self.not_equal_to = not_equal_to

    def __ne__(self, other):
        return self.not_equal_to != other.not_equal_to


obj1 = NotEqualTo(a)
obj2 = NotEqualTo(b)
print(f'{obj1.not_equal_to} != {obj2.not_equal_to} = {obj1 != obj2}')


class BitwiseAnd:
    def __init__(self, bitwise_and):
        self.bitwise_and = bitwise_and

    def __and__(self, other):
        return self.bitwise_and & other.bitwise_and


obj1 = BitwiseAnd(a)
obj2 = BitwiseAnd(b)
print(f'{obj1.bitwise_and} & {obj2.bitwise_and} = {obj1 & obj2}')


class BitwiseOr:
    def __init__(self, bitwise_or):
        self.bitwise_or = bitwise_or

    def __or__(self, other):
        return self.bitwise_or | other.bitwise_or


obj1 = BitwiseOr(a)
obj2 = BitwiseOr(b)
print(f'{obj1.bitwise_or} | {obj2.bitwise_or} = {obj1 | obj2}')


class BitwiseXor:
    def __init__(self, bitwise_xor):
        self.bitwise_xor = bitwise_xor

    def __xor__(self, other):
        return self.bitwise_xor ^ other.bitwise_xor


obj1 = BitwiseXor(a)
obj2 = BitwiseXor(b)
print(f'{obj1.bitwise_xor} ^ {obj2.bitwise_xor} = {obj1 ^ obj2}')


class BitwiseRightShift:
    def __init__(self, bitwise_right_shift):
        self.bitwise_right_shift = bitwise_right_shift

    def __rshift__(self, other):
        return self.bitwise_right_shift >> other.bitwise_right_shift


obj1 = BitwiseRightShift(a)
obj2 = BitwiseRightShift(b)
print(f'{obj1.bitwise_right_shift} >> {obj2.bitwise_right_shift} = {obj1 >> obj2}')


class BitwiseLeftShift:
    def __init__(self, bitwise_left_shift):
        self.bitwise_left_shift = bitwise_left_shift

    def __lshift__(self, other):
        return self.bitwise_left_shift << other.bitwise_left_shift


obj1 = BitwiseLeftShift(a)
obj2 = BitwiseLeftShift(b)
print(f'{obj1.bitwise_left_shift} << {obj2.bitwise_left_shift} = {obj1 << obj2}')


class IAdd:
    def __init__(self, iadd):
        self.iadd = iadd

    def __iadd__(self, other):
        self.iadd += other.iadd
        return self.iadd


obj1 = IAdd(a)
obj2 = IAdd(b)
print(f'{obj1.iadd} += {obj2.iadd} = {obj1.iadd}')


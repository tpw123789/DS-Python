

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    @staticmethod
    def gcd(m, n):
        """歐幾里得"""
        while m % n != 0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n
        return n

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __eq__(self, other):
        """
        淺相等 => 兩個物件記憶體位址相同
        深相等 => 兩個值相同
        """
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)


def test_fraction():
    a = Fraction(1, 4)
    b = Fraction(1, 4)
    c = a + b
    print(id(a))
    print(id(b))
    print(id(c))
    print(a == b)


class LogicGate:
    """BinaryGate and UnaryGate"""
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performance_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """二元門"""
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if not self.pinA:
            return int(input(f'Enter Pin A input for gate {self.get_label()} -->'))
        else:
            return self.pinA.get_from().get_output()

    def get_pin_b(self):
        return int(input(f'Enter Pin B input for gate {self.get_label()} -->'))


class UnaryGate(LogicGate):
    """一元門"""
    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def get_pin(self):
        return int(input(f'Enter Pin input for gate {self.get_label()} -->'))


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performance_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

    def set_next_pin(self, source):
        if not self.pinA:
            self.pinA = source
        else:
            if not self.pinB:
                self.pinB = source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performance_gate_logic(self):
        a = self.get_pin()
        return 1 if a == 0 else 0

    def set_next_pin(self, source):
        if not self.pin:
            self.pin = source
        else:
            raise RuntimeError('Error: NO EMPTY PINS')


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performance_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

    def set_next_pin(self, source):
        if not self.pinA:
            self.pinA = source
        else:
            if not self.pinB:
                self.pinB = source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')


# g2 = AndGate('G1')
# g2.get_output()
#
# g2 = AndGate('G2')
# g2.get_output()
#
# g3 = NotGate('G3')
# g3.get_output()


class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def test(self):
    g1 = AndGate('G1')
    g1.get_output()
    g2 = AndGate('G2')
    g2.get_output()
    g3 = OrGate('G3')
    g4 = NotGate('G4')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())


print('0123156789'.find('1'))
print('0123156789'.rfind('1'))
print('0123156789'.count('12'))

from qcpm.common.decorator import countDecorator

_reject_type = {'qreg', 'creg'}


class Operator:
    """
        eg. input: 'cx q[2],q[4]' 
            => self.type = 'cx', self.operands = [2, 4]
    """
    @countDecorator
    def __init__(self, op_type, operands, index = 0):
        if op_type in _reject_type:
            raise ValueError

        self.type = op_type
        self.index = index
        self.operands =  self._solve_operands(operands.split(','))        
    
    def _solve_operands(self, operands):
        # eg. 'q[12]' => 12
        return [int(''.join( operand.split('[')[1][:-1] ) )
                    for operand in operands]

    def __repr__(self):
        return "No: {}, {} {}".format(self.index, self.type, self.operands)
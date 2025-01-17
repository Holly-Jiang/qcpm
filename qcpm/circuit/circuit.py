from qcpm.preprocess.preprocess import preprocess
from qcpm.operator.convert import convert_type


class Circuit:
    """
        data: cx q[4],q[1]; t q[4]; t q[2]; h q[0]; ...
            => operators: [Operator, Operator ...] (eg. Operator: cx [4,1])
            => draft: ctth...(cx => c)
    """
    def __init__(self, path):
        self.operators = []
        self.draft = ''
        self._load_circuit(path)

    def _load_circuit(self, path):
        op_types = []

        for operator in preprocess(path):
            self.operators.append(operator)
            op_types.append( convert_type(operator.type) )
        
        self.draft = ''.join(op_types)

    def print(self, start=0, steps=-1):
        if steps == -1:
            steps = len(self.draft)

        for i in range(steps):
            print(self.operators[start + i])
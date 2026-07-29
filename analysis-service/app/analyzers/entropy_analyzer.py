import math



class EntropyAnalyzer:
    '''
    Calculates Shannon entropy of binary data.
    '''

    def calculate(self, data: bytes) -> float:
        '''
        We're calculating entropy in bits per byte.
        '''

        if not data:
            return 0.0

        frequencies = self._calculate_frequencies(data)

        entropy = 0.0
        total_bytes = len(data)

        for count in frequencies.values():
            probability = count / total_bytes

            entropy -= probability * math.log2(probability)

        return entropy


    def _calculate_frequencies(self, data: bytes) -> dict[int, int]:

        frequencies = {}

        for byte in data:
            frequencies[byte] = frequencies.get(byte, 0) + 1

        return frequencies
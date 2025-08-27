
class Primer:
    """
    A class representing a DNA primer.

    :param sequence: DNA sequence (A, T, C, G)
    :type sequence: str

    :ivar sequence: The primer sequence in uppercase letters.
    :type sequence: str
    :ivar length: Length of the sequence in base pairs.
    :type length: int
    :ivar tm: Calculated melting temperature (Tm, ℃).
    :type tm: float
    :ivar annealing_time: Recommended annealing time in seconds.
    :type annealing_time: int
    """
    def __init__(self, sequence:str):
        """
        Initialise a Primer object

        :param sequence: The DNA sequence (A,T,C,G)
        :return: None
        :rtype: None
        """
        self.sequence = sequence.upper()
        self.length = len(self.sequence)
        self.tm = self.calculate_tm()
        self.annealing_time = self.determine_annealing_time()

    def calculate_tm(self) -> float:
        """
        Calculate Tm (℃) of a DNA sequence.

        :return: The Tm of a DNA sequence
        :rtype: float
        """

        # Count nucleotides
        NA = self.sequence.count("A")
        NT = self.sequence.count("T")
        NC = self.sequence.count("C")
        NG = self.sequence.count("G")

        # Apply formula
        tm = (2 * (NA + NT)) + (4 * (NC + NG)) - 5

        return tm

    def determine_annealing_time(self) -> int:
        """
        Determine annealing time based on length and Tm

        :return: Time in seconds that the PCR reaction should anneal for
        :rtype: int

        """
        if self.length > 25:
            return 5
        elif self.tm >= 55:
            return 5
        else:
            return 15
    def report(self):
        """
              Generate a formatted summary of the primer.

              :return: A multi-line string containing the sequence, length, Tm, and annealing time.
              :rtype: str
              """
        return (
            f"\nSequence: {self.sequence}\n"
            f"Length: {self.length} bp\n"
            f"Tm: {self.tm} \u00b0C\n"
            f"Recommended annealing time: {self.annealing_time} sec"
        )




class Primer:
    """
    A class representing a DNA primer.

    Attributes:
        sequence (str): The DNA sequence (A,T,C,G)
        length (int): The length of the DNA sequence
        tm (float): Calculated melting temperature in Celsius
        annealing_time (int): Recommended annealing time in seconds
    """
    def __init__(self, sequence:str):
        """
        Initialise a Primer object

        Parameters:
            sequence (str) : DNA sequence (A,T,G,C)
        """
        self.sequence = sequence.upper()
        self.length = len(self.sequence)
        self.tm = self.calculate_tm()
        self.annealing_time = self.determine_annealing_time()

    def calculate_tm(self) -> float:
        """
        Calculate Tm (℃) of a DNA sequence.

        Returns:
            float: Calculated Tm in Celsius
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

        Returns:
            int: Annealing time
        """
        if self.length < 25:
            return 5
        elif self.tm >= 55:
            return 5
        else:
            return 15

if __name__ == "__main__":
    # Ask user for input
    user_seq = input("Enter a DNA sequence (A, T, C, G): ")
    primer = Primer(user_seq)

    tm_value = Primer.determine_annealing_time(primer)

    print(f"Tm value: {tm_value}")
def calculate_tm(sequence: str) -> float:
    """
    Calculate Tm (℃) of a DNA sequence.
    Formula: Tm = 2*(NA + NT) + 4*(NC + NG) - 5

    Parameters:
        sequence (str): DNA sequence (string of A, T, C, G)

    Returns:
        float: Calculated Tm in Celsius
    """
    # Convert to uppercase to avoid case issues
    seq = sequence.upper()

    # Count nucleotides
    NA = seq.count("A")
    NT = seq.count("T")
    NC = seq.count("C")
    NG = seq.count("G")

    # Apply formula
    tm = 2 * (NA + NT) + 4 * (NC + NG) - 5

    return tm


if __name__ == "__main__":
    # Ask user for input
    user_seq = input("Enter a DNA sequence (A, T, C, G): ")

    # Calculate Tm
    tm_value = calculate_tm(user_seq)

    print(f"Tm of {user_seq.upper()} = {tm_value} ℃")
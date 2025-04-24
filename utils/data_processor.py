def compute_table2(data):
    """
    Computes the values for Alpha, Beta, and Charlie using indices from table:
      - Alpha   = A5 + A20      (data[4][1] + data[19][1])
      - Beta    = A15 / A7      (data[14][1] / data[6][1])
      - Charlie = A13 * A12     (data[12][1] * data[11][1])

    Args:
        data (list[list[str, int]]): 2D list with rows in the format ["Index #", Value]

    Returns:
        dict: Dictionary with computed values (Alpha, Beta, Charlie)
    """
    try:
        # Extract values based on 0-based index positions
        alpha = data[4][1] + data[19][1]     # A5 + A20
        beta = data[14][1] / data[6][1]      # A15 / A7
        charlie = data[12][1] * data[11][1]  # A13 * A12

        return {
            "Alpha": round(alpha, 2),
            "Beta": round(beta, 2),
            "Charlie": round(charlie, 2)
        }

    except IndexError as e:
        return {
            "Alpha": "Index Error",
            "Beta": "Index Error",
            "Charlie": "Index Error"
        }
    except ZeroDivisionError as e:
        return {
            "Alpha": "-",
            "Beta": "Division by 0",
            "Charlie": "-"
        }
    except Exception as e:
        return {
            "Alpha": "Error",
            "Beta": "Error",
            "Charlie": "Error"
        }

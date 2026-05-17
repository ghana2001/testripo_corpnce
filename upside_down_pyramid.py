def print_upside_down_pyramid(rows: int) -> None:
    """Print an upside-down pyramid of stars with the given number of rows."""
    for row in range(rows, 0, -1):
        stars = '*' * (2 * row - 1)
        print(stars.center(2 * rows - 1))

if __name__ == '__main__':
    total_rows = 5
    print(f"Upside-down pyramid with {total_rows} rows:")
    print_upside_down_pyramid(total_rows)

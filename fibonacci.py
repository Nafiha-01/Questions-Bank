"""Generate Fibonacci numbers."""


def fibonacci(count: int) -> list[int]:
    """Return the first ``count`` Fibonacci numbers, starting with 0, 1.

    Args:
        count: Number of values to generate. Must be non-negative.

    Raises:
        ValueError: If ``count`` is negative.
    """
    if count < 0:
        raise ValueError("count must be non-negative")

    numbers: list[int] = []
    a, b = 0, 1
    for _ in range(count):
        numbers.append(a)
        a, b = b, a + b
    return numbers


def main() -> None:
    try:
        count = int(input("How many Fibonacci numbers? "))
        print(*fibonacci(count))
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()

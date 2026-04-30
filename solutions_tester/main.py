import logging

from runner import run_user_code


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

code = """
def fib(n):
    if n <= 2:
        return 1
    
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(int(input())))
"""


def main() -> None:
    result = run_user_code(code, "10", 5)
    print(result.success)
    print(result.output)
    print(result.used_time)


if __name__ == "__main__":
    main()

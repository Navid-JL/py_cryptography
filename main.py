import secrets


def main() -> None:
    for i in range(20):
        print(secrets.randbelow(10), end=" ")


if __name__ == '__main__':
    main()

import random

def number_game():
    answer = random.randint(1, 100)
    attempts = 0

    print("1부터 100 사이의 숫자를 맞춰보세요!")

    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("1부터 100 사이의 숫자를 입력하세요.")
                continue

            if guess < answer:
                print("더 큰 숫자입니다.")
            elif guess > answer:
                print("더 작은 숫자입니다.")
            else:
                print(f"정답입니다! 시도 횟수: {attempts}번")
                break
        except ValueError:
            print("숫자를 입력해주세요.")

if __name__ == "__main__":
    number_game()
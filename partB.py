def main():
    sm = float(input("Enter sales amount \n"))

    comm = cc(sm)

    print(f"The commision is {comm} for sales amount of {sm}")

def cc(sm):
    comm = 0.0

    if sm > 20000:
        comm += (sm - 20000) * 0.15
        sm = 20000
    if sm > 10000:
        comm += (sm - 10000) * 0.12
        sm = 10000
    if sm > 5000:
        comm += (sm - 5000) * 0.10
        sm = 5000
    if sm >= 1:
        comm += sm * 0.08

    return comm

if __name__ == "__main__":
    main()

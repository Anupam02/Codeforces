
def main():
    w = int(raw_input())
    if w > 2:
        print "YES" if w % 2 == 0 else "NO"
    else:
        print "NO"


if __name__ == '__main__':
    main()

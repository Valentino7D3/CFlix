from inputs import get_gamepad


def main():
    while 1:
        events = get_gamepad()
        for event in events:
            if("ABS_HAT0Y" == event.code):
                if(-1 == event.state):
                    print("+5s")

                if(1 == event.state):
                    print("-5s")

            if("ABS_HAT0X" == event.code):
                if(-1 == event.state):
                    print("stop")
                if(1 == event.state):
                    print("play")


if __name__ == "__main__":
    main()

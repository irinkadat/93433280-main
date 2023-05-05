def main():
    while True:
        time_ = input('Enter time: ').strip()
        try:
            cur_time = convert(time_)
            if cur_time is None:
                raise ValueError("Invalid time format")

            if 7 <= cur_time <= 8:
                print("breakfast time")
            elif 12 <= cur_time <= 13:
                print('lunch time')
            elif 18 <= cur_time <= 19:
                print('dinner time')
            else:
                pass

            break
        except ValueError:
            print('You should enter a valid time format!')


def convert(time_):

    time_ = time_.strip().split(':')

    if len(time_) != 2:
        return None

    try:
        hours = int(time_[0])
        minutes = int(time_[1])
        cur_time = hours + minutes / 60
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError("Invalid time format")

    except ValueError:
        raise ValueError("Invalid time format")
    return cur_time


if __name__ == '__main__':
    main()


# function to calculate score at a given time
def calc_score(initial_score, decrease_rate, submit_time):
    decreased_score = initial_score - (decrease_rate * submit_time)
    return max(initial_score // 2, decreased_score)


# function to calculate total score and time taken by a programmer
def calc_total_score_time(initial_scores, decrease_rates, flash_submit_times, cisco_submit_times):
    flash_score = sum([calc_score(
        initial_scores[i], decrease_rates[i], flash_submit_times[i]) for i in range(4)])
    cisco_score = sum([calc_score(
        initial_scores[i], decrease_rates[i], cisco_submit_times[i]) for i in range(4)])
    time_taken_flash = max(flash_submit_times)
    time_taken_cisco = max(cisco_submit_times)
    return flash_score, cisco_score, time_taken_flash, time_taken_cisco


# main function
def main():
    # read number of test cases
    t = int(input())
    for _ in range(t):
        # read input values
        initial_scores = list(map(int, input().split()))
        decrease_rates = list(map(int, input().split()))
        flash_submit_times = list(map(int, input().split()))
        cisco_submit_times = list(map(int, input().split()))
        # calculate total score and time taken by each programmer
        flash_score, cisco_score, time_taken_flash, time_taken_cisco = calc_total_score_time(
            initial_scores, decrease_rates, flash_submit_times, cisco_submit_times)
        # determine winner or tie
        if flash_score > cisco_score:
            print("Flash")
        elif cisco_score > flash_score:
            print("Cisco")
        else:
            if time_taken_flash < time_taken_cisco:
                print("Flash")
            elif time_taken_cisco < time_taken_flash:
                print("Cisco")
            else:
                print("Tie")


if __name__ == '__main__':
    main()

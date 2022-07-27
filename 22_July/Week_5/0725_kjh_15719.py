N = int(input())

sequence = input() + ' '

sequence_sum = 0
end_idx = -1

for _ in range(N):
    start_idx = end_idx + 1
    end_idx = sequence.find(' ', start_idx)

    sequence_sum += int(sequence[start_idx:end_idx])

correct_sequence_sum = (N - 1) * N // 2
print(sequence_sum - correct_sequence_sum)
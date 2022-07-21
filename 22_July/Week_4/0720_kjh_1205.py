rank_count, new_record, rank_limit = map(int, input().split())
ranks = list(map(int, input().split())) if rank_count > 0 else []

ranks.append(new_record)
ranks.sort(reverse=True)

rank = ranks.index(new_record) + 1

out_of_rank = len(ranks) > rank_limit and ranks[-1] == new_record
if out_of_rank:
    rank = -1

print(rank)

## 말하깔정요끔네

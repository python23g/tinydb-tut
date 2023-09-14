from db import (
    user_by_id,
    users_by_id,
    users_by_gender,
    number_of,
    users_by_country,
    users_by_city,
    users_by_nat,
    users_gt,
    users_count_gt,
    users_lt,
    users_in_range,
    users_by_country_and_city,
)

users = users_gt(70)
print(users)

count = users_count_gt(70)
print(count)

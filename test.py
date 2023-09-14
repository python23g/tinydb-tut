from db import (
    user_by_id,
    users_by_id,
    users_by_gender,
    users_by_country,
    users_by_city,
    users_by_nat,
    users_gt,
    users_lt,
    users_in_range,
    users_by_country_and_city,
)


# users = users_gt(18)  # dan katta
# users = users_lt(30)  # dan kichkina
users = users_in_range(25, 30)

print(len(users))

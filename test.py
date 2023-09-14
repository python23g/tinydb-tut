from db import (
    user_by_id,
    users_by_id,
    users_by_gender,
)


users_male = users_by_gender('male')
users_female = users_by_gender('female')

print(len(users_male))
print(len(users_female))

print(len(users_male) + len(users_female))

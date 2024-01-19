import os
import random
import string
import pickle

DataPath = os.getcwd() + "\\Data"
NameSet = set()


def summon_name(cnt: int = 100):
    NameSet.clear()

    def __rand_name() -> str:
        first_name = "".join(
            random.choice(string.ascii_uppercase)
            + "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))
            for _ in range(1)
        )

        last_name = "".join(
            random.choice(string.ascii_uppercase)
            + "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))
            for _ in range(1)
        )
        full_name = first_name + " " + last_name

        return full_name

    while len(NameSet) <= cnt:
        tmp = __rand_name()
        if tmp not in NameSet:
            NameSet.add(tmp)


summon_name()
with open(DataPath + "\\NameSet", "wb") as f:
    pickle.dump(NameSet, f)

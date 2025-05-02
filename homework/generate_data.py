"""Generate fake data with Faker."""

import csv
import os

from faker import Faker
from tqdm import tqdm  # type: ignore

fake = Faker()


def generate_fake_drivers(n):
    """Generate n fake records.

    Each record has the following fields:
    - driverId: sequential int (unique) beigning in 10
    - name: fake name
    - ssn: fake ssn
    - location: fake address
    - certified: 'Y' or 'N'
    - wage-plan: 'miles' or 'hours'

    """
    drivers = []
    for i in tqdm(range(n), desc="drivers"):
        record = {
            "driverId": i + 10,
            "name": fake.name(),
            "ssn": fake.ssn(),
            "location": fake.address(),
            "certified": fake.random_element(elements=("Y", "N")),
            "wage-plan": fake.random_element(elements=("miles", "hours")),
        }
        drivers.append(record)

    return drivers


if __name__ == "__main__":

    # Generate fake data
    fake_drivers = generate_fake_drivers(100)
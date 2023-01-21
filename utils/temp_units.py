def cel_to_far(cel_units: int):
    return (cel_units * (9/5)) + 32


def far_to_cel(far_units: int):
    return (far_units - 32) * (5/9)
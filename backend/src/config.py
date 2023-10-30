from paths import Paths

# how many seconds user programs are allowed to run for
TIMEOUT : int = 1

# how many lines after the actual start, before analysis begins
OFFSET : int = 1

# for collapsed lines
ELLIPSE : str = "·" * 3

LEADING_SPACES : int = 4

PATHS : Paths = Paths()

# create testing DataFrames
GENERATE_TEST : bool = True

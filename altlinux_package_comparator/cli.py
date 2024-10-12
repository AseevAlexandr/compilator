import json
import argparse
from package_comparator import AltLinuxPackageComparator

BRANCHES_TO_COMPARE = ['sisyphus', 'p10']

def main():
    comparator = AltLinuxPackageComparator(BRANCHES_TO_COMPARE)
    p10_diff, sisyphus_diff, version_diff = comparator.compare_brunch()

    #тут какой-то принт 
if __name__ == '__main__':
    main()

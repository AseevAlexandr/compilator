import json
import argparse
from package_comparator import AltLinuxPackageComparator


def main():
    parser = argparse.ArgumentParser(description='Compare binary packages between ALT Linux branches.')
    parser.add_argument('branches', nargs=2, choices=['sisyphus', 'p10'], help='Branches to compare')

    args = parser.parse_args()

    comparator = AltLinuxPackageComparator(args.branches)
    comparison_result = comparator.compare_packages()

    print(json.dumps(comparison_result, indent=4))


if __name__ == '__main__':
    main()

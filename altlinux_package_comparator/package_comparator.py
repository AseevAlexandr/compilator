import requests
from packaging.version import Version

class AltLinuxPackageComparator:
    BASE_URL = "https://rdb.altlinux.org/api/export/branch_binary_packages"

    def __init__(self, branches):
        self.branches = branches
        self.branches_info = {branch: self.get_branch_info(branch) for branch in branches}

    def get_branch_info(self, branch):
        response = requests.get(f"{self.BASE_URL}/{branch}")
        response.raise_for_status()
        return response.json()

    def process_data(self, branch):
        branch_packages = {}

        for package in self.branches_info[branch]['packages']:
            if branch_packages.get(package['arch']):
                branch_packages[package['arch']][package['name']] = package['release']
            else:
                branch_packages[package['arch']] = {}
        return {branch: branch_packages}

    def compare_brunch(self):
        ...



p10_packages = set(package['name'] for package in self.packages['p10']['packages'])

    def compare_packages(self):
        comparison_result = {}

        for arch in self.get_all_architectures():
            comparison_result[arch] = {
                'only_in_p10': [],
                'only_in_sisyphus': [],
                'higher_version_in_sisyphus': []
            }

            p10_packages = self.packages['p10'].get(arch, [])
            sisyphus_packages = self.packages['sisyphus'].get(arch, [])

            p10_set = {pkg['name']: pkg['version-release'] for pkg in p10_packages}
            sisyphus_set = {pkg['name']: pkg['version-release'] for pkg in sisyphus_packages}

            # Пакеты только в p10
            only_in_p10 = set(p10_set.keys()) - set(sisyphus_set.keys())
            comparison_result[arch]['only_in_p10'] = list(only_in_p10)

            # Пакеты только в sisyphus
            only_in_sisyphus = set(sisyphus_set.keys()) - set(p10_set.keys())
            comparison_result[arch]['only_in_sisyphus'] = list(only_in_sisyphus)

            # Пакеты с большей версией в sisyphus
            for pkg_name, p10_version in p10_set.items():
                if pkg_name in sisyphus_set:
                    sisyphus_version = sisyphus_set[pkg_name]
                    if Version(sisyphus_version) > Version(p10_version):
                        comparison_result[arch]['higher_version_in_sisyphus'].append(pkg_name)

        return comparison_result

    def get_all_architectures(self):
        all_arch = set()
        for branch in self.branches:
            for arch in self.packages[branch]:
                all_arch.add(arch)
        return all_arch


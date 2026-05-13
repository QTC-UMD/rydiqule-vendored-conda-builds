import toml
import json

packages = toml.load('pkgs.toml')
defaults = packages['defaults']

PLATFORM_OS_MAP = {
    'win-64':    {'os': 'windows-latest', 'arch': 'x64'},
    'osx-arm64': {'os': 'macos-latest',   'arch': 'arm64'},
    'linux':     {'os': 'ubuntu-latest',  'arch': 'x64'},
}

arch_include = []
noarch_include = []

for name, spec in packages.items():
    if name == 'defaults':
        continue
    noarch = spec.get('noarch', defaults['noarch'])
    if noarch:
        noarch_include.append({'name': name})
    else:
        platforms = spec.get('platforms', defaults['platforms'])
        pythons   = spec.get('pythons',   defaults['pythons'])
        for platform in platforms:
            os_info = PLATFORM_OS_MAP[platform]
            for python in pythons:
                arch_include.append({
                    'name':     name,
                    'os':       os_info['os'],
                    'arch':     os_info['arch'],
                    'python':   python,
                    'platform': platform,
                })

print(f"arch_matrix={json.dumps({'include': arch_include})}")
print(f"noarch_matrix={json.dumps({'include': noarch_include})}")
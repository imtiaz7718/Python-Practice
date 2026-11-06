import subprocess

# This script shows saved Wi‑Fi passwords for networks already stored on this PC.
# It does NOT reveal passwords for networks you do not own or control.

print('Saved Wi-Fi profiles and passwords on this computer:')
print('-' * 70)

profiles_output = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles'],
    text=True,
    errors='ignore'
)

profile_lines = profiles_output.splitlines()
profiles = []

for line in profile_lines:
    if 'All User Profile' in line:
        parts = line.split(':')
        if len(parts) > 1:
            profiles.append(parts[1].strip())

if not profiles:
    print('No saved Wi-Fi profiles found on this computer.')
else:
    print(f"{'Wi-Fi Name':<28} {'Password'}")
    print('-' * 70)

    for profile in profiles:
        try:
            details = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
                text=True,
                errors='ignore'
            )
        except subprocess.CalledProcessError:
            print(f"{profile:<28} {'Not available'}")
            continue

        password = ''
        for line in details.splitlines():
            if 'Key Content' in line:
                password = line.split(':', 1)[1].strip()
                break

        print(f"{profile:<28} {password if password else 'No password found'}")
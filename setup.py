from setuptools import find_packages, setup

setup(
    name='vlearn',
    version='1.0.0',
    author='Kelompok 4 RPL',
    author_email='13520103@std.stei.itb.ac.id',
    description=' '.join([
        'Package for VLearn.',
    ]),
    url='https://gitlab.informatika.org/vlearn/if2250-2021-k03-04-vlearn',
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    install_requires=[
        'PyQt5',
        'argon2-cffi',
        'faker'
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
)
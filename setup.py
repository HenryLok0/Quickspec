from setuptools import setup, find_packages

setup(
    name='quickspec',
    version='0.1.0',
    description='快速顯示電腦硬體規格的 CLI 工具',
    author='HenryLok0',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'py-cpuinfo',
    ],
    entry_points={
        'console_scripts': [
            'quickspec=quickspec.main:print_spec',
        ],
    },
    python_requires='>=3.7',
)

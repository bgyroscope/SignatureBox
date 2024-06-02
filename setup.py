import setuptools

setuptools.setup(
    name='Signature_Box',
    author='Ben Girodias',
    description='Simple signature box example.',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['tk', 'matplotlib', 'pynput', 'numpy'],  # 'pyautogui??
)
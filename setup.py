from setuptools import setup, find_packages


setup(
    author='x0x0f',
    description='GENERATE KEYWORDS FOR GOOGLE ADS',
    name='google_ads_keywords_generator',
    version='0.1.0',
    packages=find_packages(include=['google_ads_keywords_generator']),
    python_requires='>=3.6',
    install_requires=['pandas', 'click'],
    entry_points={
        'console_scripts': [
            'google_ads_keywords_generator=google_ads_keywords_generator.cli:cli'
        ],
    },
)

from setuptools import setup, find_packages

setup(
    name="httpxprof",
    version="0.1",
    packages=find_packages("httpxprof"),
    install_requires=["click", "httpx", "snakeviz", "uvicorn", "tqdm"],
    entry_points="""
        [console_scripts]
        httpxprof=httpxprof.main:cli
    """,
)

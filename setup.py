from setuptools import setup

setup(
 name="discerus",
 version="0.1.0",
 description="Machine Learning.",
 url="https://github.com/samirelanduk/discerus",
 author="Sam Ireland",
 author_email="mail@samireland.com",
 license="MIT",
 classifiers=[
  "Development Status :: 4 - Beta",
  "Intended Audience :: Science/Research",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.6",
  "Programming Language :: Python :: 3.7",
 ],
 packages=["discerus"],
 install_requires=["numpy", "pandas", "matplotlib", "jupyter"]
)

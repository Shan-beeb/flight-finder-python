# Flight Search automation 

A small automation project integrated with Selenium, and Behave(Cucumber) framework

## Installation

Just clone this repository 

## Usage

```python
To execute all tests in a feature file => behave <feature_file_name>.feature
To execute a particular scenario => behave -n "<name of the scenario or scenario outline"

To generate Allure report=>
1) behave -f allure_behave.formatter:AllureFormatter -o reports/ <either leave empty for all tests, or specify feature file or scenario name>
2) allure serve reports/ <for viewing reports>

```

## License
[MIT](https://choosealicense.com/licenses/mit/)
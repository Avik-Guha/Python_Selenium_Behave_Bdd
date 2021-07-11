# Selenium_Python_Behave_Bdd

This is a Web Automation Testing framework using:

    Selenium
    Python
    Behave BDD
    Page Object Model

## Installation

### Prerequisite:

    Python
    Pycharm
    Intellibot

### Extensions in Pycharm:

    Atom Material Icons
    Comments Highlighter
    Gherkin
    Ini
    IntelliBot@master.dev
    Kite AI Code AutoComplete: Python

All set!!! Just download the Project folder...

## Framework Structure

    .wdm --> contains browser drivers (created by driver manager)

    Base --> contains Base class (used for setting environment, browser driver, logger)

    Features --> contains cucumber feature files

        Environment.py --> contains Hooks methods

        Steps --> contains Step Definition files

    Logs --> execution logs is generated here

    Objects --> contains object locators

    Pages --> Contains Business Components and Object Locator files

    Report --> HTML report is generated using behave html formatter

    Screenshots --> used to store screenshots

    TestData --> this folder contains test data files

    Utility --> Contains custom utilities developed in the framework and are used globally across the framework

           Config_Reader --> utility built to read data from Config (cfg) file

           Excel_Reader --> utility built to read data from Excel (xlsx) file

           Json_Reader --> utility built to read data from Json file

    behave.ini --> behave configuration file

## Usage

    1. Download the Project folder

    2. Add dependency libraries
        selenium
        behave
        behave-html-formatter
        openpyxl
        jsonpath
        selenium-page-factory

    3. Run command to run the test:

        <behave_html_formatter Report>

        <Using folder name>
        behave Features -D environment=QA -D browser=Chrome --f html -o Reports/behave-report.html
        
        <Using tag>
        behave Features --tags=@Sanity -D environment=QA -D browser=Chrome -f html -o Reports/behave-report.html
        
        <Using Feature file name>
        behave Features/Registration.feature -D environment=QA -D browser=Chrome --f html -o Reports/behave-report.html

## Contributing

   Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

   Please make sure to update tests as appropriate.

## Contributors

   Avik Guha

## License

   Licensed under the [MIT License](LICENSE).

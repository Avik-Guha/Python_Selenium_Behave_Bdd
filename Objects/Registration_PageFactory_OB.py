from seleniumpagefactory.Pagefactory import PageFactory


class RegistrationPageFactory(PageFactory):

    def __init__(self, driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver
        self.highlight = True

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "username_textbox": ('CSS', "#tab-content1 > form > input:nth-child(3)"),
        "email_textbox": ('CSS', "#tab-content1 > form > input:nth-child(5)"),
        "password": ('CSS', "#tab-content1 > form > input:nth-child(7)"),
        "confirm_password_textbox": ('CSS', "#tab-content1 > form > input:nth-child(9)"),
        "date_of_birth": ('CSS', "#datepicker"),
        "phone_textbox": ('CSS', "#tab-content1 > form > input[type=text]:nth-child(13)"),
        "address": ('CSS', "#tab-content1 > form > input[type=text]:nth-child(15)"),
        "address_type_home_radio_button": ('CSS', "#tab-content1 > form > input[type=radio]:nth-child(16)"),
        "address_type_office_radio_button": ('CSS', "#tab-content1 > form > input[type=radio]:nth-child(17)"),
        "gender_dropdown": ('CSS', "#tab-content1 > form > select:nth-child(18)"),
        "country_dropdown": ('CSS', "#countryId"),
        "state_dropdown": ('CSS', "#stateId"),
        "city_dropdown": ('CSS', "#cityId"),
        "zipcode_textbox": ('CSS', "#tab-content1 > form > input[type=text]:nth-child(23)"),
        "terms_checkbox": ('CSS', "#tab-content1 > form > div > input[type=checkbox]:nth-child(1)"),
        "read_details_link": ('CSS', "#tab-content1 > form > div > em > a"),
        "sign_up_button": ('CSS', "#tab-content1 > form > div > input[type=submit]:nth-child(3)")
    }

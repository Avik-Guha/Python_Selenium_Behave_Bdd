from Base import Base
from Objects import Registration_OB
from Objects import Registration_PageFactory_OB
from Utility import Config_Reader, Json_Reader, Excel_Reader


class Registration:

    def __init__(self, driver):
        global ob_cfg_path
        global ob_json_path
        global excel_path

        self.driver = driver
        self.registration_PageFactory_OB = Registration_PageFactory_OB.RegistrationPageFactory(driver)

        ob_json_path = ".\\Objects\\Registration_OB.json"
        ob_cfg_path = "./Objects/Registration_OB.cfg"
        excel_path = ".\\TestData\\TestData.xlsx"

    def enter_username(self):
        logger = Base.set_logger()
        logger.info('Enter enter_username')
        self.driver.find_element_by_css_selector(
            Config_Reader.read_config_data(ob_cfg_path, "Registration", "username"))\
            .send_keys(Excel_Reader.read_excel_data(excel_path, "Tester", "Username"))
        logger.info('Enter Username')

    def enter_password(self):
        logger = Base.set_logger()
        self.driver.find_element_by_css_selector(
            Json_Reader.read_json_data(ob_json_path, "Registration.password"))\
            .send_keys(Excel_Reader.read_excel_data(excel_path, "Tester", "Password"))
        logger.info('Enter Password')

    def enter_confirm_password(self):
        logger = Base.set_logger()
        # Using page factory method ---> send_text()
        self.registration_PageFactory_OB.confirm_password_textbox\
            .set_text(Excel_Reader.read_excel_data(excel_path, "Tester", "Password"))

        # Using selenium method ---> send_keys()
        # self.registration_PageFactory_OB.confirm_password_textbox \
        #     .send_keys(Excel_Reader.read_excel_data(excel_path, "Tester", "Password"))
        logger.info('Enter Confirm Password')

    def enter_email(self):
        logger = Base.set_logger()
        self.driver.find_element_by_css_selector(Registration_OB.Registration["email_textbox"])\
            .send_keys(Excel_Reader.read_excel_data(excel_path, "Tester", "Email"))
        logger.info('Enter Email')

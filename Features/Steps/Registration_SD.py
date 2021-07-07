from behave import *
from Base import Base
from Pages import Registration_BC


@given('Launch application page')
def step_impl(context):
    # logger = Base.set_logger()
    context.driver.get(Base.get_environment())
    # logger.info('Step Definition -----> Launch application Pages')


@when('User enters "{item}"')
def user_enters(context, item):
    logger = Base.set_logger()
    logger.info("Entered user_enters")
    registration_obj = Registration_BC.Registration(context.driver)

    if item == "username":
        logger.info("Call ----> enter_username()")
        registration_obj.enter_username()
    elif item == "password":
        registration_obj.enter_password()
    elif item == "email":
        registration_obj.enter_email()
    elif item == "confirm password":
        registration_obj.enter_confirm_password()

    Base.wait_for_seconds(2)

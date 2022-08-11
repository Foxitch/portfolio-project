from litecart.web_ui.pages.application import Application
import allure
from datetime import datetime
from litecart.core.fixture.options import *


@pytest.fixture(scope='function')
def app(request) -> Application:
    fixture = Application()
    fixture.session.login(
        request.config.getoption('email'),
        request.config.getoption('password'),
        request.config.getoption('proto'),
        request.config.getoption('url'),
    )
    yield fixture
    allure.attach(fixture.wd.get_screenshot_as_png(),
                  name=f"Screenshot {datetime.today()}",
                  attachment_type=allure.attachment_type.PNG)
    fixture.destroy()

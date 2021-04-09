import pytest

@pytest.mark.usefixtures("setup")
class LoggedOutTest:
    pass

@pytest.mark.usefixtures("account_setup")
class LoggedInTest:
    pass

@pytest.mark.usefixtures("account_setup", "nav_new")
class UserNewTest:
    pass

@pytest.mark.usefixtures("account_setup", "nav_past")
class UserPastTest:
    pass

@pytest.mark.usefixtures("account_setup", "nav_comments")
class UserCommentsTest:
    pass

@pytest.mark.usefixtures("account_setup", "nav_ask")
class UserAskTest:
    pass

@pytest.mark.usefixtures("account_setup", "nav_show")
class UserShowTest:
    pass

@pytest.mark.usefixtures("account_setup", "nav_jobs")
class UserJobsTest:
    pass

@pytest.mark.usefixtures("account_setup", "nav_submit")
class UserSubmitTest:
    pass


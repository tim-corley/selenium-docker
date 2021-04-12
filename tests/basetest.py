import pytest

# use for navbar and submit page tests
@pytest.mark.usefixtures("account_setup")
class LoggedInTest:
    pass

@pytest.mark.usefixtures("setup")
class HomeTest:
    pass

@pytest.mark.usefixtures("setup", "nav_new")
class NewTest:
    pass

@pytest.mark.usefixtures("setup", "nav_past")
class PastTest:
    pass

@pytest.mark.usefixtures("setup", "nav_comments")
class CommentsTest:
    pass

@pytest.mark.usefixtures("setup", "nav_ask")
class AskTest:
    pass

@pytest.mark.usefixtures("setup", "nav_show")
class ShowTest:
    pass

@pytest.mark.usefixtures("setup", "nav_jobs")
class JobsTest:
    pass

@pytest.mark.usefixtures("setup", "nav_submit")
class SubmitTest:
    pass


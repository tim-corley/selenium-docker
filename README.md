<!-- PROJECT HEADER -->
<br />
<div>
<p align="center">
  <a href="https://www.selenium.dev/">
    <img src="/img/selenium.svg" alt="Selenium Logo" width="100" height="100">
  </a>
  <a href="https://www.docker.com/">
    <img src="/img/docker.svg" alt="Docker Logo" width="100" height="100">
  </a>
</p>
<h2 align="center">Distributed Testing with Selenium & Docker</h2>
<p align="center">
Fast & Stable Test Execution Done Remotely
    <br />
    <br />
    <a href="https://github.com/tim-corley/selenium-docker/issues">Report Issue</a>
</p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#test-configuration">Test Configuration</a></li>
      </ul>
    </li>
        <li>
      <a href="#running-tests">Running Tests</a>
      <ul>
        <li><a href="#locally">Locally</a></li>
        <li><a href="#remotely">Remotely</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
### About

**This repo contains boilerplate code to get up-and-running with *Distributed*, Automated UI Testing using Selenium & Docker. It is intended to be used as a foundation for writing / adding your own tests that can then be run remotely via Selenium Grid.**

### Built With

* [Selenium](https://www.selenium.dev/) - a toolset for web browser automation that uses the best techniques available to remotely control browser instances and emulate a user’s interaction with the browser
* [Selenium Grid](https://www.selenium.dev/documentation/en/grid/) - enables execution of Selenium WebDriver scripts on remote machines that can be configured with different browser types & versions
* [Docker Engine](https://docs.docker.com/engine/) - a tool to containerize applications
* [Docker Compose](https://docs.docker.com/compose/) - a tool to define & run multi-container applications
* [PyTest](https://docs.pytest.org/en/stable/) - a framework that makes building simple and scalable tests easy

<!-- GETTING STARTED -->
## Getting Started

Follow the steps below to get a local development instance up & running.

### Prerequisites

 - Python3
 - pipenv
 - Docker
 - docker-compose

### Installation

```bash
git clone
cd project_dir
pipenv shell
pipenv install
```

### Test Data

Some tests in this suite require a Hacker News account. If you do not have an account go to: [https://news.ycombinator.com/login](https://news.ycombinator.com/login)

If you already have an account (or once you've created one), you'll need to add the username and password to a `.env` file in project root.

```
USERNAME=tester_account
PASSWORD=yourpassword
```

### Test Configuration

Use the `config.json` to define how your tests are run - namely, which browser and wether to run remotely (via Selenium Grid) or locally. Supported broswer types are:
 - Chrome Local
 - Chrome Remote
 - Firefox Local
 - Firefox Remote


## Running Tests

### Locally

 - run all tests with parallelization support (2 threads) and automatically rerun failed tests (up to two times)
```
python -m pytest -n 2 --reruns 2
```

 - after test run is completed, a result report can be viewed at: `./logs/pytest_html_report.html`

### Remotely

To run test remotely, you'll need an instance of Selenium Grid running. To do some, we'll spin up some docker containers. 

 - First, download the images:
```bash 
$ docker pull selenium/hub
$ docker pull selenium/node-chrome
$ docker pull selenium/node-chrome-debug
$ docker pull selenium/node-firefox
$ docker pull selenium/node-firefox-debug
```

 - Second, be sure to have a `docker-compose.yml` file at project root. It should look like:
```yaml
version: "3"
services:
  selenium-hub:
    image: selenium/hub
    ports:
      - "4444:4444"
    environment:
      GRID_MAX_SESSION: 16
      GRID_BROWSER_TIMEOUT: 300
      GRID_TIMEOUT: 300

  chrome:
    image: selenium/node-chrome
    depends_on:
      - selenium-hub
    environment:
      HUB_PORT_4444_TCP_ADDR: selenium-hub
      HUB_PORT_4444_TCP_PORT: 4444
      NODE_MAX_SESSION: 4
      NODE_MAX_INSTANCES: 4

  firefox:
    image: selenium/node-firefox
    depends_on:
      - selenium-hub
    environment:
      HUB_PORT_4444_TCP_ADDR: selenium-hub
      HUB_PORT_4444_TCP_PORT: 4444
      NODE_MAX_SESSION: 4
      NODE_MAX_INSTANCES: 4
```

 - Third, run the containers: 
```bash
docker-compose up -d
```
   
Check that hub was successfully started by going to: [http://localhost:4444/grid/console](http://localhost:4444/grid/console)

 - Run the tests (be sure either `Chrome Remote` or `Firefox Remote` is set as browser in your config file)
```bash
python -m pytest
```

 - *if there are any issues while starting/running the tests, check the container logs for error messages:*
```
docker logs grid_docker_demo_firefox_1
```

**Scaling**

More containers can be added to the grid in order to further scale-up testing. For example, to spin up 3 Chrome containers (with 4 browser instances each as noted in the `docker-compose.yml` file):

```bash
$ docker-compose up -d --scale chrome=3
```

If you have numerous tests (and they are designed to run in parallel) with many containers running then text execute time should decrease when running tests. This example would kick off testing running via 4 threads and rerun any failures twice:
```bash
python -m pytest -n 4 --reruns 2
```

<!-- CONTACT -->
## Contact

Tim Corley | [@tcor215](https://twitter.com/tcor215) | contact@tim-corley.dev

[selenium-logo]: img/selenium.svg
[docker-logo]: img/docker.svg
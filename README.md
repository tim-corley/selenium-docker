### Install
```
git clone
cd project_dir
pipenv install
```
### Run Locally
 - run all tests with parallelization support (2 threads) and automatically rerun failed tests (up to two times)
```
python -m pytest -n 2 --reruns 2
```

 - after tests run is completed, a result report can be viewed at: `./logs/pytest_html_report.html`

### Run Remotely

using selenium grid to run tests remotely and using docker compose to spin up selenium hub with chrome & firefox nodes. 

Pull all required docker images:
```bash 
$ docker pull selenium/hub
$ docker pull selenium/node-chrome
$ docker pull selenium/node-chrome-debug
$ docker pull selenium/node-firefox
$ docker pull selenium/node-firefox-debug
```

1) **Run the containers**
```
docker-compose up -d
```
   
2) Check that hub was successfully started by going to: [http://localhost:4444/grid/console](http://localhost:4444/grid/console)

3) **Configure the test run**
Use `config.json` to determine test type (local vs. remote) and brower (Firefox or Chrome)

4) **Run tests:**
```
python -m pytest
```

*if issues, check container logs:*
```
docker logs grid_docker_demo_firefox_1
```

#### Scaling

Spin up 3 Chrome containers (with 4 browser instances each as noted in the `docker-compose.yml` file):

```
$ docker-compose up -d --scale chrome=3
```

make sure that `browser` is set to "Chrome Remote" in your config file
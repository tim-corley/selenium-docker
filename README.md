### Run Locally

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
   
2) Check that hub was successfully started by going to: (http://localhost:4444/grid/console)[http://localhost:4444/grid/console]

3) **Configure the test run**
Use `config.json` to determine test type (local vs. remote) and brower (Firefox or Chrome)

4) **Run tests:**
```
python -m pytest
```

If issues, check logs:
```
docker logs grid_docker_demo_firefox_1
```
# Weather-APP
This App Predict City Weather

## How it works?
1. Clone the repo:
    `git clone https://github.com/Ziad-kh99/Weather-APP.git`
- Then you should change working dir to the root of the repo
    `cd Weather-App`

2. Build the image based on Dockerfile:
    `docker build -t weather_app:v1 .`

3. Run the the container:
    `docker run -i --name weather-app weather-app`
- Note that the first time you need to run the container, just use command `docker start` instead of creating new container.
    `docker start -i weather-app`


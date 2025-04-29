
# moodChecker  :stuck_out_tongue_winking_eye:

AI-based face and emotion detector with Deepface and Tensorflow to detect predominant emotions in real time. Using docker for containers that allow practical and fast execution, regardless of the operating system.

---
## 📦 Features

- Faces detector, please beware of ghosts in your enviroment :ghost:
- Detector of main emotions and signaling to differentiate different subjects.
- Open for editing to integrate it into your projects.
- Dockerized for easy setup.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kur0bai/moodChecker.git
cd moodChecker
```

### 2. Run it in Docker

Docker: 
- Create an image from projects directory: `docker build -t feeling-app .`

- Add local connections to access control list:
 ```xhost +local:docker```
 
- Execute it with the require parameters to display the app and use your camera: ``` 
sudo docker run -it --rm --device=/dev/video0:/dev/video0 --env DISPLAY=$DISPLAY  --volume=/tmp/.X11-unix:/tmp/.X11-unix feeling-app```


NOTE: You can change the name of the application as you need it, this example is with `feeling-app`
You can close the app using the key `q` or stopping the execution.

<p align="left" width="100%"><img src="https://imgur.com/2FzOlQx.png" height="300" /></p>

Easy right? :fish_cake:

### Important:  :pushpin:
This face recognition could be used in projects that you consider appropriate, for example: To detect predominant emotions of patients with depressive disorders or mental alteration states, which can help prevent or identify behaviors and patterns. That later they can be solved for the improvement of individuals. 

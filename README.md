# 🚀 IA Hackathon Project

![Arduino Project](images/project.png)

Welcome to **IA Hackathon Project**! About
This project was made as part of a collaboration between **42 school** and **Lazada art school**. The goal was to make an AI with **psychiatric problems** in pairs. So we decided to make a child with tics. 🎯

![Photo](assets/images/project.jpg)

## 📌 Features  
✅ Motor activation based on python request\n
✅ Request to mistral API\n
✅ Talk to text\n
✅ Text to talk\n

---

## 🛠️ Required Components
| Component       | Quantity |
|-----------------|----------|
| Arduino Uno     | 1        |
| Motor           | 1        |
| Relais          | 1        |
| Wires           | Several  |

---

## ⚙️ Wiring Diagram
Here’s how to connect the components:  

![Schemat](assets/images/schemat.png)

📌 **Explanation:**  
- The **HC-SR04 sensor** is connected to **Trig** and **Echo** pins  
- The **motor** is connected to a **relay** on **pin D3**  
- The **Arduino** communicates via **USB** with a PC  

---

## 🖥️ Installation
1️⃣ Clone this repository:
```sh
git clone https://github.com/user/my-arduino-project.git
```

2 update motor.ino in arduino card and close the IDE Arduino (for resolve Serial problem)
3 Install all lib :
```sh
pip install requests openai-whisper sounddevice numpy soundfile pyttsx3 pygame pyserial
```
4 Replace MY_API_KEY and COM_OF_THE_ARDUINO in main.py
5 Run main.py
```sh
python main.py
```



import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
        def __init__(self):
                super().__init__() 
                self.city_label=QLabel("Enter City Name: ", self)
                self.city_input=QLineEdit(self)
                self.get_weather_button=QPushButton("Get Weather", self)
                self.temperature_label=QLabel(self)
                self.emoji_label=QLabel(self)
                self.description_label=QLabel(self)
                self.initUI()

        def initUI(self):
            self.setWindowTitle("Weather App")    

            vbox=QVBoxLayout()

            vbox.addWidget(self.city_label)
            vbox.addWidget(self.city_input)
            vbox.addWidget(self.get_weather_button)
            vbox.addWidget(self.temperature_label)
            vbox.addWidget(self.emoji_label)
            vbox.addWidget(self.description_label)

            self.setLayout(vbox)

            self.city_label.setAlignment(Qt.AlignCenter)
            self.city_input.setAlignment(Qt.AlignCenter)
            self.temperature_label.setAlignment(Qt.AlignCenter)
            self.emoji_label.setAlignment(Qt.AlignCenter)
            self.description_label.setAlignment(Qt.AlignCenter)

            self.city_label.setObjectName("city_label")
            self.city_input.setObjectName("city_input")
            self.get_weather_button.setObjectName("get_weather_button")
            self.temperature_label.setObjectName("temperature_label")
            self.emoji_label.setObjectName("emoji_label")
            self.description_label.setObjectName("description_label")

            self.setStyleSheet("""
                Qlabel, QPushButton{
                        font-family: calibri;
                               
                }
                QLabel#city_label{
                         font-size: 40px;
                         font-family: Georgia, serif;
                         font-color: blue;
                                           
                               }
                QLineEdit#city_input{
                         font-size: 30px;      
                         font-family: Georgia, serif; 
                                     }
                QPushButton#get_weather_button{
                         font-size: 30px;
                         font-weight: bold;         
                                  }   
                QLabel#temperature_label{
                         font-size:75px; 
                         font-family: Georgia, serif;            
                               }
                QLabel#emoji_label{
                         font-size: 100px;
                         font-family: Segoe UI emoji;            
                               }
                QLabel#description_label{
                         font-size: 50px;
                         font-family: Georgia, serif;        
                               }                                                                                                                       

                """)

            self.get_weather_button.clicked.connect(self.get_weather)
            
        def get_weather(self):
            api_key="8c489e3958a49622480808d23222091f"
            city=self.city_input.text()
            url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

            response=requests.get(url)
            data=response.json()
  
            if data["cod"]==200:
                self.display_weather(data)
 
        def display_error(self,message):
               pass

        def display_weather(self,data):
                temperature_k=data["main"]["temp"]
                temperature_c=temperature_k - 273.15
                weather_id=data["weather"][0]["id"]
                weather_description=data["weather"][0]["description"]
              
                self.temperature_label.setText(f"{temperature_c:.0f}°C")
                self.description_label.setText(weather_description)
                self.emoji_label.setText(self.get_weather_emoji(weather_id))

        @staticmethod
        def get_weather_emoji(weather_id):

                if 200<= weather_id <=232:
                        return "⛈️"
                elif 300 <= weather_id <=321:
                        return "🌧️"
                elif 500 <= weather_id <=531:
                        return "☔"
                elif 600 <= weather_id <=622:
                        return "❄️"
                elif 701 <= weather_id <=741:
                        return "🌁"
                elif weather_id==800:
                       return "☀️"
                elif 801 <= weather_id <=804:
                        return "☁️"
                else:
                        return ""
if __name__=="__main__":
        app=QApplication(sys.argv)                
        weather_app=WeatherApp()
        weather_app.show()
        sys.exit(app.exec_())
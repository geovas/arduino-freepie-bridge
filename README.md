# README #

### Краткое описание проекта ###

Данный проект призван обеспечить взаимодействие между Arduino UNO и программой FreePIE.

В качестве примера я реализовал следующую цепочку:
* Джойстик SJ-6000 (от Sega Mega Drive)
* Плата Arduino UNO
* Программа FreePIE (за счет библиотеки PySerial)
* Опционально: виртуальный дхойстик vJoy (v2)
* Игры (например Sonic Green Hill Paradise ACT2 и Drift Stage)

### Как запустить проект? ###

* Нужно прошить Arduino Uno скетчем "sega_joy"
* Подключить джойстик к Arduino (будет описано позже)
* Установить на ПК программы FreePIE и vJoy
* При необходимости обновить vJoy DLL в папке FreePIE
* Установить в FreePIE библиотеку PySerial (будет описано позже)
* При необходимости нужно настроить vJoy (будет описано позже)
* Запустить один из скриптов из этого репозитория в FreePIE
* Играть!

Полезная информация: 
* vJoy DLL: vJoyInterfaceWrap.dll и vJoyInterface.dll
* папка vJoy: C:\Program Files\vJoy
* папка FreePIE: C:\Program Files (x86)\FreePIE


### Ссылки ###

* Arduino Uno: https://www.arduino.cc/en/Main/ArduinoBoardUno
* FreePIE: http://andersmalmgren.github.io/FreePIE/
* vJoy: http://vjoystick.sourceforge.net/site/
* PySerial: https://pypi.python.org/pypi/pyserial/2.7
* Sonic Green Hill Paradise ACT2: https://mega.nz/#!zA1gRQiK!oECaimAgyzx198TPUCyXzUMrtp4R4juuafhDtDFOEXw
* Drift Stage: http://www.driftstagegame.com/
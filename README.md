![Windows](https://img.shields.io/badge/Windows-blue?style=for-the-badge&logo=windows)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 🏎️ Автоматическое заполнение БЭВМ

## ✨ Использование
В файл `data/commands.txt` нужно внести команды (адрес и значения) в 16-тиричной системе.

Далее нужно запустить БЭВМ и убедиться, что красным цветом горит **ИМЕННО ПЕРВАЯ** цифра.

После этого нужно запустить `run.py` и дождаться, когда скрипт завершит работу (окно станет обычного размера).

`❗ ВАЖНО`: автоматический ввод работает для окна, которое открыто в данный момент (т.е. находится на переднем плане), 
поэтому во избежание ввода не в то окно, не нажимайте ничего, пока скрипт находится в работе 

# 🛠️ Установка
* Клонируйте репо
    ```shell
  git clone https://github.com/S1riyS/auto-OPD.git
  ```
* Создайте новое виртуальное окружение
    ```shell
  python -m venv venv
  venv\Scripts\activate
  ```
* Установите в него зависимости из `requirements.txt`
    ```shell
  pip install -r requirements.txt
  ```

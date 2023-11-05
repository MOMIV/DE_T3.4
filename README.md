# DE_T3.4
Задание 3.4

Лайт-версия:

1.   Что же, вы достигли своей цели — ваши коллеги оказались в восторге от вашей разработки! Но вот незадача — теперь они бегают к вам каждые десять минут и просят запустить вашу чудо-программу, чтобы получить актуальный анализ по курсу биткоина. Вы, конечно, с радостью готовы помочь, однако этот процесс довольно утомительный и отвлекает вас от выполнения рабочих обязанностей. Но вы не спешите расстраиваться, ведь во время изучения языка Python вам как раз довелось познакомиться с таким инструментом как Airflow. И если вы все правильно поняли (а вы все правильно поняли, как всегда, ведь вы очень умны!), как раз он-то вам и должен помочь.



Так как вы уже владеете docker’ом, вы находите официальный образ Airflow и запускаете контейнеры с помощью docker-compose 

docker-compose.yml. Какое чудо, у Airflow есть свой пользовательский интерфейс, который доступен по адресу http://localhost:8080. Чтобы авторизоваться, достаточно использовать стандартную комбинацию airflow/airflow.

Обратите внимание, что в docker-compose файле, в списке сервисов уже есть пользовательская база данных — db. Она нам еще обязательно понадобится.

2.   Что же, в той папке, в которой вы запустили docker-compose up, у вас должны появиться 3 новые папки:

·       dags,

·       logs,

·       plugins.



Ключевой для нас в данном случае является папка dags, в которой мы и будем создавать наши скрипты для работы в Airflow.



3.   Вы решили начать с простого и создали самый простой dag, в котором есть всего один оператор, который выводит в стандартный вывод фразу: «Good morning my diggers!».



p.s. В данном задании нельзя использовать PythonOperator

4.   Вы все точно рассчитали — ваши коллеги ходят к вам каждые 10 минут, что же, это означает, что наш будущий dag тоже должен работать каждые 10 минут. Настройте ваш dag таким образом, чтобы он выводил фразу «Good morning my diggers!» каждые 10 минут.



p.s. Чтобы правильно настроить время, можно воспользоваться Crontab.guru - The cron schedule expression editor.

5.   Пришло время для серьезных дел: создайте в вашем dag еще один оператор, который будет воспроизводить логику работы вашего приложения по получении курсов валют и записи результатов в таблицу. Но теперь вам нужно ориентироваться не на предыдущей месяц, а просто получать значение курса на момент запуска airflow dag’a.



p.s. Создайте таблицу в уже существующей базе db.

p.s. Речь идет о приложениях, которые вы разрабатывали в задании 3.2 в пунктах 1-2.

p.s. Убедитесь в том, что в таблицу добавляются записи каждые 10 минут и с новым значением курса.

Решение:

![Image alt](https://github.com/MOMIV/DE_T3.4/raw/main/pic/1.png)

![Image alt](https://github.com/MOMIV/DE_T3.4/raw/main/pic/2.png)

![Image alt](https://github.com/MOMIV/DE_T3.4/raw/main/pic/3.png)

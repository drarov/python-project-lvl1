install: #Запуск poetry
	poetry install

brain-games: #Запуск brain-games
	poetry run brain-games

brain-even: #Запуск brain-even
	poetry run brain-even

brain-calc: #Запуск команды brain-calc чисто по названию без доп команд
	poetry run brain-calc

brain-gcd: #Запуск команды brain-gcd чисто по названию без доп команд
	poetry run brain-gcd

brain-progression: #Запуск команды brain-progression чисто по названию без доп команд
	poetry run brain-progression

brain-prime: #Запуск команды brain-prime чисто по названию без доп команд
	poetry run brain-prime

build: #активация poetry в проекте
	poetry build

publish: #отправка проекта на PyPl понарошку
	poetry publish --dry-run

package-install: #Установка пакета из операционной системы
	python3 -m pip install --user dist/*.whl

lint: #Проверка кода линтером flake8
	poetry run flake8 brain_games

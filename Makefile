install: #Start poetry
	poetry install

brain-games: #Start brain-games
	poetry run brain-games

brain-even: #Start brain-even
	poetry run brain-even

brain-calc: #Start brain-calc
	poetry run brain-calc

brain-gcd: #Start brain-gcd
	poetry run brain-gcd

brain-progression: #Start brain-progression
	poetry run brain-progression

brain-prime: #Start brain-prime
	poetry run brain-prime

build: #Activate poetry inside of the project
	poetry build

publish: #Sending the project to PyPl in dry mode
	poetry publish --dry-run

package-install: #Install the program from a OS
	python3 -m pip install --user dist/*.whl

lint: #Checking the code with flake8
	poetry run flake8 brain_games
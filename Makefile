# Author: Cameron Noupoué

# Target to run the application
run: stop
	@# Check if Docker engine and daemon are running, if not, start them
	@docker info > /dev/null 2>&1 || (echo "Starting Docker engine..." && open --background -a Docker)

	docker start db odoo

	@cd lecture_client && python3 manage.py makemigrations && python3 manage.py migrate

	@# Run the Django development server
	@(cd lecture_client && python3 manage.py runserver) &
	sleep 1
	open http://127.0.0.1:8000/

stop:
	@pid=$$(lsof -ti :8000); \
	if [ -n "$$pid" ]; then \
		echo "Stopping server on port 8000 (PID: $$pid)"; \
		kill -9 $$pid; \
	else \
		echo "No server found on port 8000"; \
	fi
